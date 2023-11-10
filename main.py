from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

filepaths = glob.glob("text/*.txt")


def read_txt(filepath):
    with open (filepath, "r") as fp:
        txt_content = fp.read()
    return txt_content


# Create pdf
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    filename = Path(filepath).stem.title()
    # Add one page per each text file
    pdf.add_page()
    # Add Title of the page
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename, ln=1)

    # get content and add it to the pdf page
    content = read_txt(filepath)
    pdf.set_font(family="Times", size=12)

    # Height corresponds to the height of each cell
    # from the multicell
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")



