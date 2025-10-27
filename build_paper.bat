@echo off
echo Building research paper...
echo.

REM Compile LaTeX document
echo Running pdflatex...
pdflatex -interaction=nonstopmode research_paper.tex
REM Continue even if there are minor warnings

REM Run BibTeX/Biber for bibliography
echo Running Biber...
biber research_paper
if errorlevel 1 (
    echo WARNING: Biber failed! Continuing anyway...
)

REM Compile again to include citations
echo Running pdflatex again...
pdflatex -interaction=nonstopmode research_paper.tex

REM Final compilation
echo Running pdflatex one more time...
pdflatex -interaction=nonstopmode research_paper.tex

REM Clean up auxiliary files
echo Cleaning up...
del *.aux *.log *.bbl *.blg *.bcf *.run.xml *.out *.toc *.fdb_latexmk *.fls *.synctex.gz 2>nul

echo.
echo Done! PDF created: research_paper.pdf
pause

