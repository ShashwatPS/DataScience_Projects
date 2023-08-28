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

# def marks(x):
#     return x/2
# print(df1['Marks'].apply(marks)) Apply method is used for passing in custom made function which in this case is marks
# df1['Half_Marks']=df1['Marks'].apply(marks) This is used for creating a new column name 'Half_Marks'


# print(df1['Marks'].apply(lambda x:x/2)) Doing the same thing as above by using lambda function
# print(df1['Name'].apply(len)) This displays the length of the Name string here.


# df1['Male_Female']= df1['Gender'].map({'Male':1,'Female':0})
# print(df1)
# Using map for encoding purposes (Male to 1 and Female to 0 in a new column in this case)

# df1['Half_Marks']=df1['Marks'].apply(lambda x:x/2)
# df1['Male_Female']= df1['Gender'].map({'Male':1,'Female':0})
# # print(df1.drop('Male_Female',axis=1)) This drops a column form the dataset named 'Male_Female'
# print(df1.drop(['Male_Female','Half_Marks'],axis=1,inplace=True))
# The above statement drops 2 columns (Could be more depends on the no.of coulmns passed in List) form the dataset and the "
# inplace=True modifies the existing data

# print(df1.columns) Prints the name of all the columns
# print(df1.index) Displays the Range of the Index

# print(df1.sort_values(by='Marks',ascending=False)) Sorts the DataFrame in descending order according to the values in 'Marks' column
# print(df1.sort_values(by=['Marks','Gender'],ascending=False))  Sorts first by 'Marks' and then according to 'Gender'

# print(df1[df1['Gender']=='Female']) Prints only those rows where 'Gender' column's value is 'Female'
# print(df1[df1['Gender']=='Female']['Name']) Prints only those names in the 'Name' column where 'Gender' column's value is 'Female'

# print(df1[df1['Gender'].isin(['Female'])][['Name','Marks']]) Same thing as above but using the isin function
