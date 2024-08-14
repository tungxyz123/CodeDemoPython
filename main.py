import pandas as pd

# Load the "website_access_category_table.csv" file
website_access_df = pd.read_csv('website_access_category_table.csv')

# Load the "sale_data.csv" file
sale_data_df = pd.read_csv('sale_data.csv')

# Load the "product_group_table.csv" file
product_group_df = pd.read_csv('product_group_table.csv')

# Load the "product_detail_data.csv" file
product_detail_df = pd.read_csv('product_detail_data.csv')

# Load the "market_trend_table.csv" file
market_trend_df = pd.read_csv('market_trend_table.csv')

# Load the "customer_data.csv" file
customer_data_df = pd.read_csv('customer_data.csv')
# Print the first few rows of each dataframe
print("website_access_df:\n", website_access_df.head())
print("sale_data_df:\n", sale_data_df.head())
print("product_group_df:\n", product_group_df.head())
print("product_detail_df:\n", product_detail_df.head())
print("market_trend_df:\n", market_trend_df.head())
print("customer_data_df:\n", customer_data_df.head())

# Check the data types of the columns
print("website_access_df data types:\n", website_access_df.dtypes)
print("sale_data_df data types:\n", sale_data_df.dtypes)
print("product_group_df data types:\n", product_group_df.dtypes)
print("product_detail_df data types:\n", product_detail_df.dtypes)
print("market_trend_df data types:\n", market_trend_df.dtypes)
print("customer_data_df data types:\n", customer_data_df.dtypes)
# Check for missing values
print("website_access_df missing values:\n", website_access_df.isnull().sum())
print("sale_data_df missing values:\n", sale_data_df.isnull().sum())
print("product_group_df missing values:\n", product_group_df.isnull().sum())
print("product_detail_df missing values:\n", product_detail_df.isnull().sum())
print("market_trend_df missing values:\n", market_trend_df.isnull().sum())
print("customer_data_df missing values:\n", customer_data_df.isnull().sum())

# Handle missing values (e.g., drop rows with missing data or fill with appropriate values)
website_access_df = website_access_df.dropna()
sale_data_df = sale_data_df.dropna()
product_group_df = product_group_df.fillna(0)
product_detail_df = product_detail_df.fillna('Unknown')
market_trend_df = market_trend_df.dropna()
customer_data_df = customer_data_df.fillna('Unknown')
# Convert date columns to datetime format
website_access_df['AccessDate'] = pd.to_datetime(website_access_df['AccessDate'])
sale_data_df['SaleDate'] = pd.to_datetime(sale_data_df['SaleDate'])
product_group_df['CreationDate'] = pd.to_datetime(product_group_df['CreationDate'])
product_group_df['LastUpdatedDate'] = pd.to_datetime(product_group_df['LastUpdatedDate'])
market_trend_df['TrendStartDate'] = pd.to_datetime(market_trend_df['TrendStartDate'])
market_trend_df['TrendEndDate'] = pd.to_datetime(market_trend_df['TrendEndDate'])
customer_data_df['DateOfBirth'] = pd.to_datetime(customer_data_df['DateOfBirth'])
customer_data_df['RegistrationDate'] = pd.to_datetime(customer_data_df['RegistrationDate'])

# Convert numeric columns to appropriate data types
website_access_df['Duration'] = website_access_df['Duration'].astype(float)
sale_data_df['Quantity'] = sale_data_df['Quantity'].astype(int)
sale_data_df['TotalAmount'] = sale_data_df['TotalAmount'].astype(float)
product_detail_df['Price'] = product_detail_df['Price'].astype(float)
product_detail_df['StockQuantity'] = product_detail_df['StockQuantity'].astype(int)
# Check for and remove duplicate rows
print("Duplicate rows in website_access_df:", website_access_df.duplicated().sum())
print("Duplicate rows in sale_data_df:", sale_data_df.duplicated().sum())
print("Duplicate rows in product_group_df:", product_group_df.duplicated().sum())
print("Duplicate rows in product_detail_df:", product_detail_df.duplicated().sum())
print("Duplicate rows in market_trend_df:", market_trend_df.duplicated().sum())
print("Duplicate rows in customer_data_df:", customer_data_df.duplicated().sum())

website_access_df = website_access_df.drop_duplicates()
sale_data_df = sale_data_df.drop_duplicates()
product_group_df = product_group_df.drop_duplicates()
product_detail_df = product_detail_df.drop_duplicates()
market_trend_df = market_trend_df.drop_duplicates()
customer_data_df = customer_data_df.drop_duplicates()