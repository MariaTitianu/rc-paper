# Installation Guide for Windows

## Problem

The Python package `pdflatex` is **NOT** the actual LaTeX compiler. You need to install a LaTeX distribution.

## Solution Options

### Option 1: Install MiKTeX (Recommended for Windows) ✅

1. **Download MiKTeX:**
   - Go to: https://miktex.org/download
   - Download the installer (click "Download" button)

2. **Install:**
   - Run the installer
   - Choose: "Install packages on-the-fly: Yes"
   - Choose: "Paper size: A4"
   - Click "Start" to install

3. **Add to PATH (usually automatic, but if not):**
   - Find installation folder (usually `C:\Program Files\MiKTeX\miktex\bin\x64`)
   - Add to Windows PATH:
     - Press Windows Key, search "Environment Variables"
     - Edit "Path" variable
     - Add: `C:\Program Files\MiKTeX\miktex\bin\x64`
     - Click OK

4. **Restart Terminal/PowerShell**

5. **Verify Installation:**
   ```powershell
   pdflatex --version
   ```

### Option 2: Install TeX Live (Alternative)

1. **Download TeX Live:**
   - Go to: https://www.tug.org/texlive/
   - Download and run `install-tl-windows.exe`

2. **Follow installer (takes ~30 minutes)**
3. **Restart Terminal**

### Option 3: Use Overleaf Online (Easiest!) 🚀

**No installation needed!**

1. Go to: https://www.overleaf.com
2. Create free account
3. Create new project → Upload Project
4. Upload these files:
   - `research_paper_enhanced.tex`
   - `references.bib`
5. Set main file: `research_paper_enhanced.tex`
6. Click "Recompile"
7. Download PDF

This is the **fastest option** and works from any device!

### Option 4: Use VS Code with LaTeX Workshop Extension

1. **Install VS Code:** https://code.visualstudio.com/
2. **Install MiKTeX** (see Option 1)
3. **Install LaTeX Workshop extension** in VS Code
4. Open `.tex` file → Click "Recompile" button

## After Installation

Once you have `pdflatex` installed, compile your paper:

### Method 1: Use the batch file
```powershell
.\build_paper.bat
```

### Method 2: Manual compilation
```powershell
pdflatex research_paper_enhanced.tex
biber research_paper_enhanced
pdflatex research_paper_enhanced.tex
pdflatex research_paper_enhanced.tex
```

### Method 3: Using latexmk (after installing MiKTeX)
```powershell
latexmk -pdf research_paper_enhanced.tex
```

## Verify Installation

Run these commands to check if everything is installed:

```powershell
# Check LaTeX
pdflatex --version

# Check bibliography
biber --version

# Check if all tools are available
where pdflatex
where biber
```

## Quick Start Summary

**Easiest:** Use Overleaf.com (no installation!)

**Best for offline:** Install MiKTeX → Double-click `build_paper.bat`

## Troubleshooting

### "pdflatex not recognized"
- Install MiKTeX or TeX Live
- Restart terminal/PowerShell
- Check PATH environment variable

### "Package not found" errors
- MiKTeX will prompt to install missing packages automatically
- Click "Install" when prompted

### "Biber not found"
- Install `biber` package separately or use TeX Live (includes biber)
- Or use `bibtex` instead of `biber`

## Need Help?

- **Overleaf Help:** https://www.overleaf.com/learn
- **MiKTeX FAQ:** https://docs.miktex.org/manual/faq.html
- **LaTeX Community:** https://latex.org/forum/

