#!/bin/bash

# LaTeX research paper build script for Linux/Mac

echo "Building research paper..."
echo

# Check if file argument is provided
if [ -z "$1" ]; then
    TEXFILE="research_paper_enhanced.tex"
else
    TEXFILE="$1"
fi

echo "Compiling: $TEXFILE"

# First compilation
echo "Running pdflatex (first pass)..."
pdflatex -interaction=nonstopmode "$TEXFILE" || { echo "ERROR: pdflatex failed!"; exit 1; }

# Run Biber for bibliography
echo "Running Biber..."
biber "${TEXFILE%.tex}" 2>/dev/null || echo "WARNING: Biber not found or failed. Skipping bibliography."

# Second compilation
echo "Running pdflatex (second pass)..."
pdflatex -interaction=nonstopmode "$TEXFILE"

# Third compilation
echo "Running pdflatex (third pass)..."
pdflatex -interaction=nonstopmode "$TEXFILE"

# Clean up auxiliary files
echo "Cleaning up auxiliary files..."
rm -f *.aux *.log *.bbl *.blg *.bcf *.run.xml *.out *.toc *.fdb_latexmk *.fls *.synctex.gz 2>/dev/null

echo
echo "Done! PDF created: ${TEXFILE%.tex}.pdf"

