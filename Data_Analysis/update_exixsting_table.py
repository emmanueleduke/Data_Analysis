import pandas as pd

# Read the existing Excel file into a DataFrame
excel_file_path = r'C:/Users/Emmanuel/Desktop/table_example.xlsx'
sheet_name = 'Sheet1'  # Replace with the actual sheet name
df = pd.read_excel(excel_file_path, sheet_name)

# Update the DataFrame as needed
# For example, update a specific cell
row_index = 1
column_name = 'Task'
new_value = 'Find'
df.at[row_index, column_name] = new_value

# Write the updated DataFrame back to the Excel file
df.to_excel(excel_file_path, sheet_name, index=False)
