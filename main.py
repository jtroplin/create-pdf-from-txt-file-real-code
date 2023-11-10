from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob("text/*.txt")


def read_txt(filepath):
    with open (filepath, "r") as fp:
        content = fp.read()
    return content


pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    content = read_txt(filepath)
    filename = Path(filepath).stem.title()
    pdf.add_page()
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=50, h=8, txt=filename, ln=1)

pdf.output("output.pdf")



