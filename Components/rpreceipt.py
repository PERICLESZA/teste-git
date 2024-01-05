import streamlit as st
import time
import os
from datetime import datetime
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus.tables import Table
import base64
from streamlit_javascript import st_javascript
import Controllers.customerController as customerC


def displayPDF(file_name, ui_width):
    # Read file as bytes:
    with open(file_name, "rb") as file:
        bytes_data = file.read()
    # Convert to utf-8
    base64_pdf = base64.b64encode(bytes_data).decode('utf-8')
    # Embed PDF in HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width={str(ui_width)} height={str(ui_width*4/3)} type="application/pdf"></iframe>'
    # Display file
    st.markdown(pdf_display, unsafe_allow_html=True)

def mainRpReceipt(oExchange, id_customer):

    doc = SimpleDocTemplate("receipt.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)
    Story = []

    now = datetime.now()

    # name   = 'Péricles Zacarias Abrahão'
    # phone  = '41 9964-5905'
    # loja = "**4th**"

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    formatted_time = time.ctime()

    styles.add(ParagraphStyle(fontSize=11, name='Center', alignment=TA_CENTER))
    styles.add(ParagraphStyle(fontSize=25, name='Center1', alignment=TA_CENTER))
    styles.add(ParagraphStyle(fontSize=15, name='Right', alignment=TA_RIGHT))
    styles.add(ParagraphStyle(fontSize=20, name='Centerfoot', alignment=TA_CENTER))

    Story.append(Paragraph('''<b>Exchange</b>''', styles["Center1"]))
    Story.append(Spacer(1, 50))
    
    dCustomer = customerC.get_det_customer(id_customer)
   
    line1 = ("Name:", dCustomer['name'])
    line2 = ("Phone:", dCustomer['phone'])
    line3 = ("Ck$:", format(round(oExchange[4], 2), ",.2f"))
    line4 = ("Disc$:", round(oExchange[5]+oExchange[7]+oExchange[8]+oExchange[9],2))
    line5 = ("Pagado$:", format(round(oExchange[11],2),",.2f"))
    line6 = ("Data$:", oExchange[1] + " - " + oExchange[2])
    line7 = ("Nº:", oExchange[0]) # 0 idcashflow
    line8 = ("", "")
    line9 = ("*Data saved by:", st.session_state.login)

    data = [line1, line2, line3, line4, line5, line6, line7, line8, line9]
    patientdetailstable = Table(data)
    patientdetailstable.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
    ]))

    Story.append(patientdetailstable)
    Story.append(Spacer(1, 5))
    Story.append(Paragraph("**" + st.session_state.nmstore + "**", styles["Center"]))
    Story.append(Spacer(1, 5))
    Story.append(Paragraph('El valor máximo de descuento es 3.0% + centavos', styles["Center"]))
    Story.append(Spacer(1, 30))
    Story.append(Paragraph('''<b>LUNA TRAVEL</b>''', styles["Centerfoot"]))
    Story.append(Spacer(1, 20))
    Story.append(Paragraph('(415 457-3864)', styles["Centerfoot"]))

    Story.append(Spacer(1, 12))

    doc.build(Story)

    pdf_file_name = 'receipt.pdf'
    ui_width = st_javascript("window.innerWidth")
    displayPDF(pdf_file_name, ui_width - 10)


    