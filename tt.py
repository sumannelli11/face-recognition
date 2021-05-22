import pandas as pd
base_file = 'D:\\HDF\\Abhilash\\'
data = pd.read_csv(base_file+"IB MAIZE.csv")
print(data.columns)