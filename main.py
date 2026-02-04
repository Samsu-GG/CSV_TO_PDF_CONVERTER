import fpdf
import pandas as pd

pdf = fpdf.FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False,margin=0)


df = pd.read_csv("topics.csv")

for index,row in df.iterrows():

    pdf.add_page()

    pdf.set_font("Arial",style="B",size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(200,10,txt=row["Topic"],ln=1,align="L")
    pdf.line(10,20,200,20)

    pdf.ln(263)
    pdf.set_font("Arial",style="I",size=12)
    pdf.set_text_color(180,180,180)
    pdf.cell(0,10,txt=row["Topic"],ln=0,align="R")

    for i in range(26):
        pdf.line(10, 20+((i+1)*10), 200, 20+((i+1)*10))


    for i in range(int(row["Pages"])-1):
        pdf.add_page()
        for j in range(27):
            pdf.line(10, 20 + (j * 10), 200, 20 + (j * 10))
        pdf.ln(273)
        pdf.set_font("Arial", style="I", size=12)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 10, txt=row["Topic"], ln=0, align="R")



pdf.output("topics.pdf")





