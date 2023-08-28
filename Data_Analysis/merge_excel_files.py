import pandas as pd

def merge_excel_files(filenames, sheetnames, output_filename):
    all_data = []

    for file, sheet in zip(filenames, sheetnames):
        df = pd.read_excel(file, sheet_name=sheet)
        all_data.append(df)

    merged_data = pd.concat(all_data, ignore_index=True)
    merged_data.to_excel(output_filename, index=False)

folder_path = r'C:/Users/Emmanuel/Desktop/'

files = [folder_path + 'London Data.xlsx',
         folder_path + 'Birminghan Data.xlsx',
         folder_path + 'Briston Data.xlsx']

sheet_names = ['N', 'Sheet1', 'Sheet1']  # Use the correct sheet names

output_filename = folder_path + 'Master Data.xlsx'

# Call the function to merge the Excel files
merge_excel_files(files, sheet_names, output_filename)

print("Merging complete. Master Data.xlsx created.")

