### Dynamic LaTeX Subsections Generation

This repository demonstrates how to dynamically populate repeated LaTeX subsections from Python. Below you’ll find:

---

#### Folder Structure

```plaintext
my_latex_project/
├── main.tex               # The main LaTeX file
├── generated_subsections/ # Directory for auto-generated .tex files
│   ├── subsection_1.tex
│   ├── subsection_2.tex
│   └── ...
├── generate_content.py    # Python script that creates subsection_#.tex
└── compile_to_pdf.py      # Python script that compiles main.tex to PDF

- main.tex: Contains the fixed LaTeX layout and uses \input{...} to bring in each subsection's content.
- generated_subsections/: Populated by generate_content.py with one file per subsection.
- generate_content.py: Python script that performs the calculations and writes LaTeX snippets into the .tex files.
- compile_to_pdf.py: Python script that compiles main.tex into a PDF via pdflatex.
