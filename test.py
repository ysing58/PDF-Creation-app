from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():

    for i in range(row["Pages"]):

        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100,100,100)
        pdf.cell(h=12, w=0, align="L", ln=1, border=0, txt=row["Topic"])
        pdf.line(10, 22, 200, 22)
        pdf.ln(265)
        pdf.set_font(family="Times", style="B", size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(h=10, w=0, align="R", ln=1, border=0, txt=row["Topic"])

pdf.output("output.pdf")