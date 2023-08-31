import pandas as pd 

df = pd.read_excel(r"C:\Users\Emmanuel\Desktop\output.xlsx",engine="openpyxl")

results = df.iloc[:5,2:5]
print(results)
