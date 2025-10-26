#!/usr/bin/env python3
"""
LaTeX Research Paper Compilation Helper
This script helps compile your LaTeX document.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a shell command and return success status."""
    print(f"\n{'='*60}")
    print(f"{description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            print(f"✓ {description} - SUCCESS")
            return True
        else:
            print(f"✗ {description} - FAILED")
            if result.stderr:
                print("\nError output:")
                print(result.stderr)
            return False
            
    except Exception as e:
        print(f"✗ {description} - ERROR: {e}")
        return False

def check_requirements():
    """Check if required tools are installed."""
    tools = ['pdflatex', 'biber']
    missing = []
    
    print("\n" + "="*60)
    print("Checking for required tools...")
    print("="*60)
    
    for tool in tools:
        try:
            subprocess.run(
                [tool, '--version'],
                capture_output=True,
                check=True
            )
            print(f"✓ {tool} - Found")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print(f"✗ {tool} - NOT FOUND")
            missing.append(tool)
    
    return missing

def main():
    """Main compilation function."""
    # Default file
    tex_file = "research_paper_enhanced.tex"
    
    if len(sys.argv) > 1:
        tex_file = sys.argv[1]
    
    if not Path(tex_file).exists():
        print(f"Error: File '{tex_file}' not found!")
        print("\nAvailable .tex files:")
        for f in Path('.').glob('*.tex'):
            print(f"  - {f}")
        return 1
    
    print("\n" + "="*60)
    print("LaTeX Research Paper Compiler")
    print("="*60)
    print(f"Compiling: {tex_file}")
    print(f"Working directory: {os.getcwd()}")
    
    # Check for required tools
    missing_tools = check_requirements()
    
    if missing_tools:
        print("\n❌ Missing required tools:")
        for tool in missing_tools:
            print(f"   - {tool}")
        print("\nPlease install a LaTeX distribution:")
        print("   Windows: Download MiKTeX from https://miktex.org/download")
        print("   Or use Overleaf.com online (no installation needed)")
        print("\nSee INSTALLATION_GUIDE.md for detailed instructions.")
        return 1
    
    # Base filename without extension
    base_name = Path(tex_file).stem
    
    # Compilation sequence
    commands = [
        (f'pdflatex -interaction=nonstopmode "{tex_file}"', 
         f"LaTeX Compilation (Pass 1/3)"),
        (f'biber {base_name}', 
         "Bibliography Processing"),
        (f'pdflatex -interaction=nonstopmode "{tex_file}"', 
         f"LaTeX Compilation (Pass 2/3)"),
        (f'pdflatex -interaction=nonstopmode "{tex_file}"', 
         f"LaTeX Compilation (Pass 3/3)"),
    ]
    
    # Run compilation sequence
    for cmd, desc in commands:
        if not run_command(cmd, desc):
            print(f"\n❌ Compilation failed at: {desc}")
            print("\nCheck the error messages above.")
            return 1
    
    # Check if PDF was created
    pdf_file = f"{base_name}.pdf"
    if Path(pdf_file).exists():
        print("\n" + "="*60)
        print(f"✅ SUCCESS! PDF created: {pdf_file}")
        print("="*60)
        
        # Ask if user wants to open the PDF
        try:
            if sys.platform == 'win32':
                os.startfile(pdf_file)
            elif sys.platform == 'darwin':
                subprocess.run(['open', pdf_file])
            else:
                subprocess.run(['xdg-open', pdf_file])
        except Exception:
            pass  # Silently fail if can't open
        
        return 0
    else:
        print(f"\n❌ PDF file not found: {pdf_file}")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nCompilation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)

