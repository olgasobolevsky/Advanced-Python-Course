import os
import webbrowser

from filestack import Client
from fpdf import FPDF


class PdfReport:
    """
    Generate pdf file with report about how much each flatmate should pay.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_payment = str(round(flatmate1.pays(bill=bill, co_flatmate=flatmate2), 2))
        flatmate2_payment = str(round(flatmate2.pays(bill=bill, co_flatmate=flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert icon
        pdf.image(name='house.png', w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align='C', ln=1)

        # Insert period
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert the payment of flatmate1
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=flatmate1_payment, border=0, ln=1)

        # Insert the payment of flatmate2
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=25, txt=flatmate2_payment, border=0, ln=1)

        # Create the pdf file
        pdf.output(self.filename)

        # Open the file
        #webbrowser.open('file://' + os.path.realpath(self.filename))

        webbrowser.open(self.filename)


class FileSharer:
    def __init__(self, filepath, api_key='AFQSSK1euRLqwMbqRmBlvz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
