import pandas as pd

data = pd.read_csv("../DataSets/SFsalaries.csv", low_memory=False)

print(data)