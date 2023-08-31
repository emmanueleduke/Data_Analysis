import openpyxl

book = openpyxl.load_workbook(r"C:\Users\Emmanuel\Desktop\output.xlsx")

sheet = book["Code with Simplearn"]

for row in sheet.iter_rows(min_row=1, max_row=5, max_col=6, min_col=1, values_only=True):
    print (row)
