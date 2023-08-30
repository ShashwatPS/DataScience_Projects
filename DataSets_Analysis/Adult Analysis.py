import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('../DataSets/Adult.csv')

# 1.Display Top 10 Rows of The Dataset
print(data.head(10))

# 2. Check Last 10 Rows of The Dataset
print(data.tail(10))

# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print("Rows: ",data.shape[0])
print("Columns: ",data.shape[1])

# 4. Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print(data.info)

# 5. Fetch Random Sample From the Dataset (50%)
print(data.sample(frac=0.50,random_state=100))

# 6.Check Null Values In The Dataset
# print(data.isnull().sum(axis=1)) For Rows
print(data.isnull().sum())
sns.heatmap(data.isnull())

# 7.Perform Data Cleaning [ Replace '?' with NaN ]


# 8. Drop all The Missing Values
# 9. Check For Duplicate Data and Drop Them