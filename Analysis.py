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

# print(df1['Gender'].unique()) Returns the unique values in that particular column which in this case is ['Male','Female'] in gender column

# print(df1['Gender'].nunique()) This returns the no of unique value in that particular not those particular values

# print(df1['Gender'].value_counts()) It displays the count of unique Values

# print(df1[df1['Marks']>=90]) Displays those students having marks >=90 in the 'Marks' column
# print(df1[(df1['Marks']>=90) & (df1['Marks']<=100)]) Displays those students having marks in between 90 and 100 (inclusive)
# print(df1['Marks'].between(90,100)) By default the students having marks in between 90 and 100 (inclusive) in the 'Marks' column
# print(sum(df1['Marks'].between(90,100))) It displays the no.of students having marks in between 90 and 100 (inclusive) in the 'Marks' column

# print(df1['Marks'].mean()) Returns the mean of that particular column works only for numeric data.
# print(df1['Marks'].min()) Returns the minimum value in that particular column
# print(df1['Marks'].min()) Returns the maximum value in that particular column

