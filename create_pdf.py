import subprocess

def compile_latex_to_pdf(tex_filename):
    """
    Compiles a .tex file to PDF using pdflatex (requires LaTeX installed).
    """
    try:
        # Run pdflatex twice to ensure references are updated if needed
        subprocess.run(["pdflatex", tex_filename], check=True)
        subprocess.run(["pdflatex", tex_filename], check=True)
        print("PDF successfully generated.")
    except subprocess.CalledProcessError as e:
        print(f"Error during LaTeX compilation: {e}")

if __name__ == "__main__":
    compile_latex_to_pdf("pd_development_report.tex")