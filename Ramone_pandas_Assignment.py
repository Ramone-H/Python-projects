import pandas as pd
import matplotlib

# Part 2

# storing the csv file in a data frame
df = pd.read_csv("Sales Data File.csv")

# printing the csv file
print(df)
print()

# creating a revenue column

df['Revenue'] = (df['Unit Price '] * df['Quantity'])

print(df)
print()

# Part 3: Questions and Answers

#  1.	Calculate the total revenue for the company.

total_revenue = df['Revenue'].sum()

print("The total revenue is $", total_revenue)
print()

# 2.	Calculate the total revenue for each product.

product_groupby = df.groupby(['Product'])  # group by object for products

product_revenue_total = product_groupby['Revenue'].sum()  # product and total revenue

print(product_revenue_total)
print()

# 3. Find the date with the highest total revenue.

date_groupby = df.groupby(['Date'])  # groupby object for dates

date_total_revenue = date_groupby['Revenue'].sum()  # date and total revenue

date_total_revenue_max_value = date_groupby['Revenue'].sum().max()  # outputs the max value only

filter_max = date_groupby['Revenue'].sum() == date_total_revenue_max_value  # Create a filter for the highest revenue

print(date_total_revenue[filter_max])  # Prints the date that has the higest total revenue and the amount

print()

# 4 product with the highest total revenue


product_total_revenue_max_value = product_groupby['Revenue'].sum().max()  # max revenue for product

filter_max2 = product_revenue_total == product_total_revenue_max_value  # Create a filter for the highest revenue

print(product_revenue_total[filter_max2])  # Prints the date that has the highest total revenue and the amount
print()

# 5.	Calculate the average quantity sold for each product.

average_quantity_sold = product_groupby['Quantity'].mean()
print(average_quantity_sold)
print()

# 6.	Find the date with the highest total quantity sold.

date_total_quantity_sold = date_groupby['Quantity'].sum()  # Date and sum of quantity sold

date_total_quantity_sold_max_value = date_groupby['Quantity'].sum().max()  # max quantity sold

filter_max3 = date_total_quantity_sold == date_total_quantity_sold_max_value  # mask

print(date_total_quantity_sold[filter_max3])
print()

# 7.	Determine the product with the highest total quantity sold.

product_total_quantity_sold = product_groupby['Quantity'].sum()  # product and sum of quantity sold

product_total_quantity_sold_max_value = product_groupby['Quantity'].sum().max()  # max quantity sold

filter_max4 = product_total_quantity_sold == product_total_quantity_sold_max_value  # mask

print(product_total_quantity_sold[filter_max4])
print()

# 8.	Display all products with quantity sold greater than 5
filter_max5 = product_total_quantity_sold > 5  # mask
print(product_total_quantity_sold[filter_max5])
print()

# 9.	Display the number of products with quantity sold greater than 5
print("The number of product that has sold more than 5 is: ", product_total_quantity_sold[filter_max5].count())
print()

# 10.	Display the unique products
print(df['Product'].unique())
print()

# 11.	Count the number of unique products
print(df['Product'].nunique())
print()

# 12.	Display the product name, “total quantity sold and average quantity sold” along with “total revenue sold and
# average revenue sold”

total_quantity_sold = product_total_quantity_sold

total_revenue_sold = product_revenue_total

average_revenue_sold = product_groupby['Revenue'].mean()


df1 = pd.DataFrame(total_quantity_sold)
df1.rename(columns={'Quantity':'Total Quantity Sold'}, inplace=True)
df2 = pd.DataFrame(average_quantity_sold)
df2.rename(columns={'Quantity':'Average Quantity Sold'}, inplace=True)
df3= pd.DataFrame(total_revenue_sold)
df3.rename(columns={'Revenue':'Total revenue Sold'}, inplace=True)
df4=pd.DataFrame(average_revenue_sold)
df4.rename(columns={'Revenue':'Average revenue Sold'}, inplace=True)

Display1= pd.concat([df1,df2,df3,df4],axis=1)

pd.options.display.max_columns= 5

print(Display1)