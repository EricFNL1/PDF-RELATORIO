import pandas as pd
from fpdf import FPDF


data_atualizada_imagem = {
    "Nosso N°.": ["0000000.","1111111","22222222","3333333 "],
    "Comp.": ["01/08/2024", "01/08/2024", "01/08/2024", "01/08/2024"],
    "Venc.": ["01/08/2024", "01/08/2024", "01/08/2024", "01/08/2024"],
    "Pag.": ["05/08/2024", "05/08/2024", "05/08/2024", "05/08/2024"],
    "Crédito": ["05/08/2024", "05/08/2024", "05/08/2024", "05/08/2024"],
    "Bloco": ["01","01","01","01"],
    "Unidade": ["101", "102", "103", "104"],
    "Descr.": ["BOLETO", "BOLETO", "BOLETO", "BOLETO"],
    "Plano": ["QUOTAS", "QUOTAS", "QUOTAS", "QUOTAS"],
    "Valor": [400.00, 420.00, 410.00, 430.00],
    "Pago": [0, 0, 0, 0],
    "Juros": [2.00, 1.50, 3.00, 2.50],
    "Multas": [10.00, 15.00, 12.00, 14.00],
    "Honorários": [50.00, 55.00, 60.00, 52.00],
    "Correção": [5.00, 4.00, 6.00, 5.50],
    "Total": [537.50, 563.90, 572.45, 575.98]
}


df = pd.DataFrame(data_atualizada_imagem)


total_row = {
    "Nosso N°.": "TOTAL",
    "Comp.": "",
    "Venc.": "",
    "Pag.": "",
    "Crédito": "",
    "Bloco": "",
    "Unidade": "",
    "Descr.": "",
    "Plano": "",
    "Valor": df["Valor"].sum(),
    "Pago": df["Pago"].sum(),
    "Juros": df["Juros"].sum(),
    "Multas": df["Multas"].sum(),
    "Honorários": df["Honorários"].sum(),
    "Correção": df["Correção"].sum(),
    "Total": df["Total"].sum()
}


df = pd.concat([df, pd.DataFrame([total_row])], ignore_index=True)

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()


pdf.image("images.jpeg", x=10, y=4, w=33)

pdf.set_xy(8, 7)
pdf.set_font("Arial", size=11, style="B")
pdf.cell(200, 10, txt="Relatório de Arrecadação Detalhada", ln=True, align="C",)

pdf.set_xy(8, 20)
pdf.set_font("Arial", size=11, style="B")
pdf.cell(200, 10, txt="Condomínio Teste", ln=True, align="C",)


pdf.set_font("Arial", size=6, style="B")

pdf.set_xy(10, 35)
column_widths = {
    "Nosso N°.": 15,
    "Comp.": 14,
    "Venc.": 14,
    "Pag.": 14,
    "Crédito": 14,
    "Bloco": 9,
    "Unidade": 11,
    "Descr.": 13,
    "Plano": 13,
    "Valor": 15,
    "Pago": 6,
    "Juros": 8,
    "Multas": 10,
    "Honorários": 13,
    "Correção": 10,
    "Total": 13
}


for column in df.columns:
    pdf.cell(column_widths[column], 8, column, 1, 0, 'C')
pdf.ln()


pdf.set_font("Arial", size=6)
for index, row in df.iterrows():
    for col in df.columns:
        pdf.cell(column_widths[col], 8, str(row[col]), 1, 0, 'C')
    pdf.ln()


pdf.output("relatorio_Juros.pdf")