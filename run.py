import streamlit as st
import pandas as pd
print('hello world')

####### Pre processing ######
df = pd.read_csv('Webull_Orders_Records-copy.csv')
df.sort_values(['Name', 'Side'], inplace=True)
# Filter cancelled orders
df = df[df['Filled'] > 0]
# df = df[df['Symbol'] == 'NNDM']
# df = df[df['Side'] == 'Sell']
df.drop(['Status', 'Filled', 'Avg Price', 'Time-in-Force',
        'Placed Time'], axis=1, inplace=True)

# remove @ on the price column and convert to numeric
df['Price'] = pd.to_numeric(df['Price'].str[1:], errors='raise')
df['Filled Time'] = pd.to_datetime(df['Filled Time'], errors='raise')

# put total
df['Total Price'] = df['Total Qty'] * df['Price']
df.to_csv('web2.csv')

######### doing analysis on data #########
currency = "${:,.2f}".format(df['Total Price'].sum())
print(currency)

buys = df[df['Side'] == 'Buy']
sells = df[df['Side'] == 'Sell']

print('buy')
print(buys.describe(include=['object']))

print('sell')
print(sells.describe(include=['object']))

# ######### Streamlit  ###########
# st.dataframe(df)
