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

# print(df1.shape) (7, 3)
