import xlwings as xw 

wk = xw.books.open(r"C:\Users\Emmanuel\Desktop\output.xlsx")

sheet = wk.sheets('Code with Simplearn')

rg = sheet.range('A1:C2')
print(rg.value)
