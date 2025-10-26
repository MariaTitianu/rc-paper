# Research Paper LaTeX Template

This repository contains comprehensive LaTeX templates for writing research papers.

## Files

- `research_paper.tex` - Basic LaTeX document (single column)
- `research_paper_enhanced.tex` - Advanced template with algorithms, code listings, and two-column layout
- `references.bib` - Bibliography file with comprehensive examples
- `build_paper.bat` - Windows batch script for easy compilation
- `README.md` - This file

## Templates Overview

### Basic Template (`research_paper.tex`)
- Single-column layout
- Clean and simple structure
- Ideal for longer papers or book chapters

### Enhanced Template (`research_paper_enhanced.tex`)
- Two-column conference/journal style
- Algorithm pseudocode support
- Code listings with syntax highlighting
- More theorem environments
- Ablation studies and detailed experimental sections
- Professional formatting

## Structure

Both templates include:

1. **Title and Abstract** - Title, author information, keywords, and abstract
2. **Introduction** - Motivation, research questions, contributions
3. **Related Work** - Literature review and positioning
4. **Methodology** - Research design, algorithms, implementation
5. **Experiments** - Datasets, baselines, quantitative/qualitative results
6. **Discussion** - Interpretation, limitations, threats to validity
7. **Conclusion** - Summary and future directions
8. **Bibliography** - References section
9. **Appendices** - Additional materials

## Quick Start

### Windows
1. Double-click `build_paper.bat` to compile
2. Or use the commands below in terminal

### Manual Compilation

#### Using pdflatex
```bash
pdflatex research_paper_enhanced.tex
biber research_paper_enhanced
pdflatex research_paper_enhanced.tex
pdflatex research_paper_enhanced.tex
```

#### Using latexmk (recommended)
```bash
latexmk -pdf research_paper_enhanced.tex
```

#### Using Overleaf (Online)
1. Upload files to Overleaf.com
2. Main file: `research_paper_enhanced.tex`
3. Compiler: pdfLaTeX
4. Compile and download PDF

## Features

### Enhanced Template Features

- **Two-column layout** for conference/journal submissions
- **Algorithm pseudocode** using `algorithm` package
- **Code snippets** with syntax highlighting
- **Tables** with professional formatting (booktabs)
- **Mathematical notation** with AMS packages
- **Theorem environments** (theorem, lemma, proposition, corollary, definition, example)
- **Hyperlinks** with colored references
- **Subfigures** for multiple images
- **Professional tables** with top/mid/bottom rules

### Bibliography Management

The `references.bib` file includes templates for:
- Journal articles
- Conference papers
- Books and chapters
- Technical reports
- Online resources
- Preprints (arXiv)
- Software citations
- Standards
- PhD thesis

## Customization

### 1. Metadata
Edit at the top of the `.tex` file:
```latex
\title{Your Title}
\author{Your Name\footnote{Institution}}
```

### 2. Abstract and Keywords
Update with your research summary.

### 3. Content
Replace example content with your actual research.

### 4. References
Add your references in `references.bib` and cite them:
- `\cite{key}` - inline citation
- `\parencite{key}` - parentheses
- `\footcite{key}` - footnote

### 5. Figures
```latex
\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{figure.png}
    \caption{Your caption}
    \label{fig:myfigure}
\end{figure}
```

### 6. Algorithms
The enhanced template includes algorithm support - see example in `research_paper_enhanced.tex`

### 7. Code Listings
Use the `lstlisting` environment for code snippets with syntax highlighting.

## Paper Sections Explained

### Introduction
- **Motivation**: Why this work matters
- **Research Questions**: What you're answering
- **Contributions**: What you're adding
- **Organization**: Paper structure overview

### Related Work
- Categorize existing work
- Identify gaps your work addresses
- Position your contribution

### Methodology
- Problem formulation with equations
- Algorithm description
- Theoretical analysis (proofs)
- Implementation details

### Experimental Evaluation
- Datasets and statistics
- Baselines for comparison
- Evaluation metrics
- Quantitative results tables
- Qualitative analysis figures
- Ablation studies

### Discussion
- Interpret results
- Acknowledge limitations
- Discuss threats to validity
- Outline future work

### Conclusion
- Summarize contributions
- Highlight significance
- Suggest future directions

## Tips for Writing

### Abstract (150-250 words)
- Context: Why this work matters
- Problem: What you're addressing
- Method: Brief methodology
- Results: Key findings with numbers
- Impact: Why it matters

### Introduction
- Start broad, narrow to your problem
- Clearly state contributions
- Outline paper structure

### Methodology
- Be detailed enough for replication
- Include algorithm pseudocode
- Explain design choices
- Provide theoretical grounding

### Results
- Report metrics with statistical significance
- Use clear, informative tables
- Include qualitative examples
- Perform ablation studies

### Discussion
- Interpret what results mean
- Be honest about limitations
- Discuss generalizability
- Suggest specific future work

## Requirements

### Software
- LaTeX distribution:
  - **TeX Live** (recommended for Linux/Windows)
  - **MiKTeX** (Windows)
  - **MacTeX** (macOS)
- Editor options:
  - **Overleaf** (online, free)
  - **TeXstudio** (offline)
  - **VS Code** with LaTeX Workshop extension
  - **LyX** (visual editor)

### Packages
Already included in templates:
- `amsmath`, `amssymb` - Math
- `graphicx` - Images
- `hyperref` - Links
- `biblatex` - Bibliography
- `algorithm` - Pseudocode (enhanced only)
- `listings` - Code (enhanced only)

## Citation Commands

```latex
\cite{key}           % Basic citation [1]
\parencite{key}       % Parentheses (Smith 2023)
\footcite{key}        % Footnote
\citeauthor{key}      % Author name only
\citetitle{key}       % Title only
\citeyear{key}        % Year only
```

## Common Issues

### Bibliography not compiling?
1. Make sure `references.bib` exists
2. Run `biber` (or `bibtex` if using natbib)
3. Run `pdflatex` twice after bibliography

### Missing packages?
Install missing packages using your LaTeX distribution's package manager.

### Table too wide?
- Use `\resizebox{0.9\textwidth}{!}{...}`
- Or use `tabular*` environment
- Consider shortening column headers

### Algorithm not compiling?
Switch from `algorithmic` to `algpseudocode` package.

## Resources

- [Overleaf LaTeX Documentation](https://www.overleaf.com/learn)
- [BibTeX Entry Types](https://www.bibtex.com/e/entry-types/)
- [LaTeX Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics)
- [PGF/TikZ for Diagrams](https://www.overleaf.com/learn/latex/pgf-tikz)

## License

Free to use for your research!

Good luck with your research paper! 📄
