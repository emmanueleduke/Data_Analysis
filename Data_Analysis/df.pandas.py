import pandas as pd 

df = pd.read_excel(r"C:\Users\Emmanuel\Desktop\output.xlsx",engine="openpyxl")

results = df.columns
print(results)
