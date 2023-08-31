import xlwings as xw 

wk = xw.books.open(r"C:\Users\Emmanuel\Desktop\output.xlsx")

sheet = wk.sheets('Code with Simplearn')

sheet.range('a8').value = "hello xlwings"
