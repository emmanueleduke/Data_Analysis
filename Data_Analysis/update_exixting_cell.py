import openpyxl
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook['sheet_name']
sheet.cell(row=16, column=2, value= 'Customer satisfaction and comment')

# Save changes
workbook.save(excel_file_path)

# Close the workbook
workbook.close()
