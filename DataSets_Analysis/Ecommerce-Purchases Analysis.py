import pandas as pd

data = pd.read_csv("../DataSets/EcommercePurchases.csv")

# 1. Display Top 10 Rows of The Dataset
print(data.head(10))

# 2. Check Last 10 Rows of The Dataset
print(data.tail(10))

# 3. Check Datatype of Each Column
print(data.dtypes)

# 4. Check null values in the dataset
print(data.isnull().sum())

# 5. How many rows and columns are there in our Dataset?
print(data.shape)
print("Rows: ",data.shape[0])
print("Columns: ",data.shape[1])

# 6. Highest and Lowest Purchase Prices.
print("Highest: ",data['Purchase Price'].max())
print("Lowest: ",data['Purchase Price'].min())

# 7. Average Purchase Price
print(data['Purchase Price'].mean())

# 8. How many people have French 'fr' as their Language
print(len(data[data['Language']=='fr']))

# 9. Job Title Contains Engineer
print(len(data[data['Job'].str.contains('engineer', case=False)]))

# 10. Find The Email of the person with the following IP Address: 132.207.160.22
print(data[data['IP Address']=='132.207.160.22']['Email'])

# 11. How many People have Mastercard as their Credit Card Provider and made a purchase above 50?
print(len(data[(data['CC Provider']=='Mastercard') & (data['Purchase Price']>50)]))

# 12. Find the email of the person with the following Credit Card Number: 4664825258997302
