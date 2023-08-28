import openpyxl

workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook[sheet_name]

# Get values from cells A1 and B1
cell_C2 = sheet['C2'].value
cell_E2 = sheet['E2'].value
cell_C3 = sheet['C3'].value
cell_E3 = sheet['E3'].value
cell_C4 = sheet['C4'].value
cell_E4 = sheet['E4'].value
cell_C5 = sheet['C5'].value
cell_E5 = sheet['E5'].value
cell_C6 = sheet['C6'].value
cell_E6 = sheet['E6'].value


sheet.cell(row=1, column=6, value= 'Result')
# Perform arithmetic operation (addition)
result = cell_C2 + cell_E2
result1 = cell_C3 + cell_E3
result2 = cell_C4 + cell_E4
result3 = cell_C5 + cell_E5
result4 = cell_C6 + cell_E6

# Update the result in cell C1
sheet['F2'].value = result
sheet['F3'].value = result1
sheet['F4'].value = result2
sheet['F5'].value = result3
sheet['F6'].value = result4


# Save changes
workbook.save(excel_file_path)

# Close the workbook
workbook.close()

