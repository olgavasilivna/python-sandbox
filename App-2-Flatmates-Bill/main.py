from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

amount = float(input("Hey user, enter the bill amount: "))
period = input("What is the bill period? E.g. December 2020: ")

name1 = input("Enter name: ")
days_in_house1 = int(input(f"how many days did {name1} stay in the house during {period}? "))

name2 = input("Enter name: ")
days_in_house2 = int(input(f"how many days did {name2} stay in the house during {period}? "))

the_bill = Bill(amount = amount, period = period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(name1, flatmate1.pays(the_bill, flatmate2))
print(name2, flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)

api_key = input("Please enter your API key: ")
if api_key:
    file_sharer = FileSharer(filepath=pdf_report.filename, api_key=api_key)
    file_url = file_sharer.share()
    if file_url:
        print(f"File shared at: {file_url}")
    else:
        print("File sharing failed.")
else:
    print("Provide api_key to create public url.")
