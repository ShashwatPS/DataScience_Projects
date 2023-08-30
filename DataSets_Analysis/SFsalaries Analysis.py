import numpy as np
import pandas as pd

data = pd.read_csv("../DataSets/SFsalaries.csv", low_memory=False)

# 1.  Display Top 10 Rows of The Dataset
print(data.head(10))

# 2. Check Last 10 Rows of The Dataset
print(data.tail(10))

# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print(data.shape)
print("Rows: ",data.shape[0])
print("Columns: ",data.shape[1])

# 4.  Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print(data.info())

# 5. Check Null Values In The Dataset
print(data.isnull().sum())

# 6. Drop ID, Notes, Agency, and Status Columns
data.drop(['Id','Notes','Agency','Status'],axis=1)
print(data.head(1))

# 7. Get Overall Statistics About The Dataframe
print(data.describe(include='all'))

# 8. Find Occurrence of The Employee Names  (Top 5)
print(data['EmployeeName'].value_counts())

# 9. Find The Number of Unique Job Titles
# print(len(data['JobTitle'].unique()))
print(data['JobTitle'].nunique())

# 10.Total Number of Job Titles Contain Captain
# print(len(data[data['JobTitle'].str.contains('Captain',case=False)]))
print(data[data['JobTitle'].str.contains('Captain',case=False)].count())

# 11. Display All the Employee Names From Fire Department
print(data[data['JobTitle'].str.contains('fire',case=False)]['EmployeeName'])

# 12. Find Minimum, Maximum, and Average BasePay
print(data['BasePay'].describe())

# 13. Replace 'Not Provided' in EmployeeName' Column to NaN
data['EmployeeName']=data['EmployeeName'].replace('Not provided',np.nan)
print(data['EmployeeName'])

# 14. Drop The Rows Having 5 Missing Values


# 15. Find Job Title of ALBERT PARDINI
# 16. How Much ALBERT PARDINI Make (Include Benefits)?
# 17.Display Name of The Person Having The Highest BasePay
# 18.Find Average BasePay of All Employee Per Year
# 19. Find Average BasePay of All Employee Per JobTitle
# 20. Find Average BasePay of Employee Having Job Title ACCOUNTANT
# 21. Find Top 5 Most Common Jobs