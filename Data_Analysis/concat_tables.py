import pandas as pd

# List of Excel files to merge
excel_files = [
    r'C:\path\to\file1.xlsx',
    r'C:\path\to\file2.xlsx',
    r'C:\path\to\file3.xlsx'
]

# Read each Excel file into separate DataFrames
dataframes = []
for file in excel_files:
    df = pd.read_excel(file)  # You can specify sheet_name if needed
    dataframes.append(df)

# Concatenate or merge the DataFrames into a single DataFrame
merged_dataframe = pd.concat(dataframes, ignore_index=True)  # You can use merge() for more complex merging

# Write the merged DataFrame to a new Excel file
output_excel_file = r'C:\path\to\output\merged_data.xlsx'
merged_dataframe.to_excel(output_excel_file, index=False)

