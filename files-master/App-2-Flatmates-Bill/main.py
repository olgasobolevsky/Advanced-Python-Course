from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

input_amount = float(input("Please, enter bill amount: "))
input_period = input("Please, enter bill period. E.g. December 2020: ")
input_name1 = input("Please, enter name of the first flatmate: ")
input_days1 = int(input(f"Please, enter number of days in the house for {input_name1}: "))
input_name2 = input("Please, enter name of the other flatmate: ")
input_days2 = int(input(f"Please, enter number of days in the house for {input_name2}: "))

the_bill = Bill(amount=input_amount, period=input_period)
flatmate1 = Flatmate(name=input_name1, days_in_house=input_days1)
flatmate2 = Flatmate(name=input_name2, days_in_house=input_days2)
print(flatmate1.name, "pays ", flatmate1.pays(bill=the_bill, co_flatmate=flatmate2), " , ",
      flatmate2.name, "pays ", flatmate2.pays(bill=the_bill, co_flatmate=flatmate1))
pdf_report = PdfReport(f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

file_sharer = FileSharer( filepath=pdf_report.filename )
print(file_sharer.share())

