import latex_generator
import subprocess

image_path = "./img/img.jpg"
image_latex = latex_generator.generate_latex_image(image_path)

table_data = [
    ["Name", "Age", "Gender"],
    ["John", 25, "Male"],
    ["Alice", 30, "Female"],
    ["Bob", 28, "Male"]
]
table_latex = latex_generator.generate_latex_table(table_data)

latex_content = f"""
\\documentclass{{article}}
\\usepackage{{graphicx}}
\\usepackage[export]{{adjustbox}}

\\begin{{document}}

{table_latex}
{image_latex}

\\end{{document}}
"""
with open("artifacts/output.tex", "w") as file:
    file.write(latex_content)

subprocess.run(["pdflatex", "output.tex"], cwd="artifacts")

