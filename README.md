# Android Security Architecture Research Paper

Research paper analyzing Android platform security mechanisms, protection architectures, and vulnerability patterns.

## Overview

**Title**: Arhitectura de Securitate a Platformei Android: Analiza Mecanismelor de Protecție

**Authors**: Budiul Cristian-Carol, Titianu Maria

**Course**: Rețele de Calculatoare (RC) - Master's Program

## Project Structure

```
rc-paper/
├── research_paper.tex          # Main LaTeX document
├── research_paper.pdf          # Compiled output
├── references.bib              # Bibliography database
├── android_architecture.png    # Architecture diagram
├── build_paper.bat             # Windows build script
├── references/                 # Reference PDF papers
└── [extracted_papers]/         # Markdown conversions of source materials
```

## Requirements

### LaTeX Distribution
- **MiKTeX** (Windows) - Recommended
- **TeX Live** (Linux/macOS)
- **MacTeX** (macOS)

### Required Packages
All packages are included in the document and will be auto-installed by MiKTeX:
- `babel` (Romanian language support)
- `biblatex` (Bibliography management)
- `graphicx`, `subcaption` (Figures)
- `booktabs` (Tables)
- `algorithm`, `algpseudocode` (Algorithms)
- `listings` (Code snippets)
- `hyperref` (Hyperlinks)

## Installation

### 1. Install MiKTeX (Windows)

```bash
# Download from https://miktex.org/download
# Or via winget:
winget install MiKTeX.MiKTeX
```

### 2. Clone Repository

```bash
git clone <repository-url>
cd rc-paper
```

### 3. Install Missing Packages

On first compilation, MiKTeX will prompt to install missing packages. Select "Install" for automatic installation.

## Compilation

### Option 1: Claude Code + VSCode Auto-Compile (Recommended)

1. Install VSCode with "LaTeX Workshop" extension
2. Open project folder in VSCode (enables auto-compile on save)
3. Use Claude Code CLI to edit `research_paper.tex`:
   ```bash
   claude
   # Then request edits like:
   # "Add a new section about SELinux"
   # "Fix the table formatting in section 4"
   # "Add citation for the QuadRooter paper"
   ```
4. Claude Code saves changes → VSCode auto-compiles → PDF updates
5. View generated PDF in VSCode or external viewer

### Option 2: Windows Batch Script

```bash
# Double-click or run in terminal:
build_paper.bat
```

This script:
1. Runs `pdflatex` (first pass)
2. Runs `biber` (bibliography processing)
3. Runs `pdflatex` (second pass for citations)
4. Runs `pdflatex` (final pass for cross-references)
5. Cleans auxiliary files

### Option 3: Manual Compilation

```bash
# Full compilation sequence:
pdflatex research_paper.tex
biber research_paper
pdflatex research_paper.tex
pdflatex research_paper.tex
```

### Option 4: Using latexmk

```bash
# Automatic recompilation on changes:
latexmk -pdf -pvc research_paper.tex

# Single compilation:
latexmk -pdf research_paper.tex
```

## Usage

### Editing the Paper with Claude Code

1. Start Claude Code in the project directory:
   ```bash
   cd rc-paper
   claude
   ```

2. Request edits in natural language:
   ```
   "Add a paragraph about Android sandboxing in section 2"
   "Create a comparison table for security mechanisms"
   "Fix the citation format for reference [5]"
   "Translate this section to Romanian"
   ```

3. Claude Code edits `research_paper.tex` directly
4. VSCode detects changes and auto-compiles to PDF
5. Review generated `research_paper.pdf`

### Adding Citations

1. Add BibTeX entries to `references.bib`:

```bibtex
@article{key2024,
  author  = {Author Name},
  title   = {Article Title},
  journal = {Journal Name},
  year    = {2024},
  volume  = {10},
  pages   = {1--20}
}
```

2. Cite in document:

```latex
According to recent research \cite{key2024}, ...
```

### Adding Figures

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.9\columnwidth]{image.png}
    \caption{Description}
    \label{fig:label}
\end{figure}
```

### Adding Tables

```latex
\begin{table}[htbp]
    \centering
    \caption{Table Title}
    \begin{tabular}{lcc}
        \toprule
        Column 1 & Column 2 & Column 3 \\
        \midrule
        Data & Data & Data \\
        \bottomrule
    \end{tabular}
    \label{tab:label}
\end{table}
```

## Paper Content

### Key Sections
1. **Abstract** - Research summary and contributions
2. **Introduction** - Android platform overview and motivation
3. **Security Architecture** - Multi-layered protection mechanisms
4. **Vulnerability Analysis** - Common attack vectors and case studies
5. **Comparative Analysis** - Security mechanism effectiveness
6. **Case Study** - QuadRooter vulnerability analysis
7. **Conclusions** - Findings and future directions

### Research Focus Areas
- Android platform architecture
- Permission system and sandboxing
- SELinux implementation
- Application signing mechanisms
- Known vulnerabilities (QuadRooter, etc.)
- Security evolution across Android versions

## Troubleshooting

### Bibliography Not Appearing

```bash
# Ensure biber runs successfully:
biber research_paper
# Check for errors in research_paper.blg
```

### Missing Package Errors

MiKTeX should auto-install. If not:
```bash
# Open MiKTeX Console
# Settings → Install missing packages: Yes
```

### Romanian Characters Not Displaying

Ensure UTF-8 encoding:
```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[romanian]{babel}
```

### PDF Not Updating

1. Close PDF viewer
2. Delete auxiliary files: `*.aux *.bbl *.bcf *.log`
3. Recompile

## Cleaning Build Files

```bash
# Windows:
del *.aux *.log *.bbl *.blg *.bcf *.run.xml *.out *.toc *.fdb_latexmk *.fls *.synctex.gz

# Linux/macOS:
rm -f *.aux *.log *.bbl *.blg *.bcf *.run.xml *.out *.toc *.fdb_latexmk *.fls *.synctex.gz
```

## Contributing

1. Create a new branch for changes
2. Edit LaTeX source files
3. Test compilation
4. Submit pull request with compiled PDF

## License

Academic research paper - All rights reserved by authors.

## Contact

For questions regarding this research:
- Budiul Cristian-Carol
- Titianu Maria

Master's Program - Computer Networks (RC)
