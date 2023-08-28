import pandas as pd

# Read Excel files into DataFrames
file1 = pd.read_excel(r'C:\path\to\file1.xlsx')
file2 = pd.read_excel(r'C:\path\to\file2.xlsx')

# Merge the DataFrames based on a common column
merged_data = pd.merge(file1, file2, on='common_column_name', how='inner')  # Use 'how' parameter to specify merge type

# Write the merged DataFrame to a new Excel file
output_excel_file = r'C:\path\to\output\merged_data.xlsx'
merged_data.to_excel(output_excel_file, index=False)

