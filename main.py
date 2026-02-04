import fpdf
import pandas as pd

pdf = fpdf.FPDF(orientation='P',unit='mm',format='A4')

df = pd.read_csv("topics.csv")

for index,row in df.iterrows():

    pdf.add_page()

    pdf.set_font("Arial",style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(200,10,txt=row["Topic"],ln=1,align="L")
    pdf.line(10,20,200,20)

    for i in range(int(row["Pages"])-1):
        pdf.add_page()

pdf.output("topics.pdf")





