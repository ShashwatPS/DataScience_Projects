import pandas as pd

dict1 ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv',
                'Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male',
                         'Female','Female']
               }
df1=pd.DataFrame(dict1)

# print(df1) Prints the Database

# print(df1.head(x)) Prints the first x rows from the top in the dataset

# print(df1.tail(x)) Prints the last x rows from the bottom in the dataset

# print(df1.shape) => Prints no.of rows and columns in the form of an tuple in this case it is (7, 3).
# print('Number of rows',df1.shape[0]) => In this case it prints 7
# print('Number of columns', df1.shape[1]) => In this case it prints 3

# print(df1.info()) Give alot of info about no of rows and columns and its Datatype/Memory Requirement

# print(df1.isnull()) Checks the null values in Dataset
# print(df1.isnull().sum())/print(df1.isnull().sum(axis=0)) Will display the null values count column wise
# print(df1.isnull().sum(axis=1)) Will display the null values count row wise

# print(df1.describe()) By default it displays statistics for numerical columns only
# print(df1.describe(include='all')) This include='all' forces it to include all the columns




