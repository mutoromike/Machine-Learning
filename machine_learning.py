import pandas as pd

file_path = 'Files/housing.csv'
data = pd.read_csv(file_path)
print(data.head())