import pandas as pd


file_path = 'C:\\Users\\Lenovo\\Desktop\\Psychoactive-Compounds-Analysis\\data\\computed_descriptors.csv'
data = pd.read_csv(file_path)

print("Dataset 1 Columns:", data.columns.tolist())
print()

rows_data, cols_data = data.shape
print("Dataset 1 has", rows_data, "rows and", cols_data, "columns")
first_row = data.iloc[10]
for column, value in first_row.items():
    print(f"{column}: {value}")
