import os

file_path = r'D:\Ecommerce-Sales-Analysis\data\sales_data.csv'

print("File exists:", os.path.exists(file_path))

if os.path.exists(file_path):
    print("File size (in bytes):", os.path.getsize(file_path))

    with open(file_path, 'r') as f:
        content = f.read()
        print("\nFile Content Preview:")
        print(content)


import os
import pandas as pd

print("Current Working Directory:", os.getcwd())

file_path = r'D:\Ecommerce-Sales-Analysis\data\sales_data.csv'
df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df['Total_Sales'] = df['Total_Sales'].fillna(df['Total_Sales'].mean())

# Convert Date
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Remove invalid dates
df = df.dropna(subset=['Date'])

print("\nData cleaned successfully.")

print("\nTotal Revenue:", df['Total_Sales'].sum())
print("Average Sale:", df['Total_Sales'].mean())

print("\nSales by Category:")
print(df.groupby('Category')['Total_Sales'].sum())

print("\nTop 3 Products:")
print(df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False).head(3))

print("\nSales by City:")
print(df.groupby('City')['Total_Sales'].sum())


import matplotlib.pyplot as plt

# Sales by Category Bar Chart
category_sales = df.groupby('Category')['Total_Sales'].sum()

plt.figure()
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

# Sales by City Bar Chart
city_sales = df.groupby('City')['Total_Sales'].sum()

plt.figure()
city_sales.plot(kind='bar')
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.show()


plt.figure()
category_sales.plot(kind='bar')
plt.title("Sales by Category (2025)")
plt.xlabel("Category")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Create Month column
df['Month'] = df['Date'].dt.month

monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure()
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()
