import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 28],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Specify the Excel file path
output_excel_file = output_excel_file = r'C:/Users/Emmanuel/Desktop/table_example.xlsx'


# Write the DataFrame to an Excel file
df.to_excel(output_excel_file, index=False)

# Open the Excel file using pandas
excel_writer = pd.ExcelWriter(output_excel_file, engine='xlsxwriter')
df.to_excel(excel_writer, index=False, sheet_name='Sheet1')

# Get the xlsxwriter workbook and worksheet objects
workbook = excel_writer.book
worksheet = excel_writer.sheets['Sheet1']

# Get the dimensions of the DataFrame
num_rows, num_cols = df.shape

# Create a table object
worksheet.add_table(0, 0, num_rows, num_cols - 1, {'columns': [{'header': col} for col in df.columns]})

# Save the Excel file
excel_writer.save()

print(f"Table created in {output_excel_file}")

