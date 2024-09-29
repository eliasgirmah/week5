import pandas as pd

# Load the data
data = pd.read_csv('Pictures/telegram_text_data1.txt')


# Display the first few rows
print(data.head())

# Get basic info about the DataFrame
print(data.info())

# Check for missing values
print(data.isnull().sum())


data['Message Date'] = pd.to_datetime(data['Message Date'])


import pandas as pd
df = pd.DataFrame(data)

# Cleaning steps
# 1. Trim Whitespaces
df['Channel Title'] = df['Channel Title'].str.strip()
df['Channel Username'] = df['Channel Username'].str.strip()
df['Message Text'] = df['Message Text'].str.strip()

# 2. Handle Special Characters
df['Channel Title'] = df['Channel Title'].str.replace('®', '', regex=False)

# 3. Standardize Date Formats
df['Message Date'] = pd.to_datetime(df['Message Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

# 4. Remove Duplicate Entries
df.drop_duplicates(subset=['Message ID'], inplace=True)

# 5. Normalize Text Fields
df['Message Text'] = df['Message Text'].str.lower()

# 6. (Optional) Extract price from Message Text
df['Price'] = df['Message Text'].str.extract(r'Price (\d+ birr)')[0]

# Display cleaned DataFrame
print(df)

df

df['Message Text'].head()

df.to_csv('Pictures/ethio_brand_data_cleaned.csv', index=False)

# Load data into a DataFrame
df = pd.read_csv( )

# Define the characters to remove
special_characters_pattern = r'[📌✅🏢⚠️❌🆕#🎁❎"]'

# Clean the Message Text
df['Message Text'] = df['Message Text'].str.replace('\n', ' ').str.replace(special_characters_pattern, '', regex=True).str.strip()

# Save the cleaned DataFrame to a CSV file
df.to_csv('Pictures/2_ethio_brand_data_cleaned.csv', index=False)

import pandas as pd
from io import StringIO  # Make sure to import StringIO

import pandas as pd
import re  # Import the regular expressions module

# Assuming you've already loaded your DataFrame into df
# For example:
# df = pd.read_csv('your_file.csv')

# Define the special characters you want to remove
special_characters_pattern = r'[📌✅🏢⚠️❌🆕#🎁❎🌻🌼‼ እሁድ ሁሌም ክፍት ነን or call🌟📱👔|👖\(አዲስ የገባ\)"]'

# Remove special characters from the 'Message Text' column
df['Message Text'] = df['Message Text'].apply(lambda x: re.sub(special_characters_pattern, '', str(x)))



# Load the CSV file
df = pd.read_csv('Pictures/2_ethio_brand_data_cleaned.csv')

# Define a pattern to remove only the specified unwanted phrases
specific_phrases_pattern = r'(@sofonias12|‼ እሁድ ሁሌም ክፍት ነን ‼|or call)'

# Clean the 'Message Text' column by removing the specified phrases
df['Message Text'] = df['Message Text'].apply(lambda x: re.sub(specific_phrases_pattern, '', str(x)))

# Remove any extra whitespace that may have been left behind
df['Message Text'] = df['Message Text'].str.strip()



# Adjust pandas option to prevent truncation
pd.set_option('display.max_colwidth', None)

# Now display the full content
df.head()

# Split the 'Message Text' into multiple columns using string methods
df['Product Name'] = df['Message Text'].str.split('\r\n').str[0]
df['Size'] = df['Message Text'].str.extract(r'size ([\d,]+)')
df['Price'] = df['Message Text'].str.extract(r'price (\d+ birr)')
df['Address'] = df['Message Text'].str.extract(r'አድራሻ-(.*) or call')
df['Phone'] = df['Message Text'].str.extract(r'or call (\d+)')

# Display the resulting DataFrame
pd.set_option('display.max_colwidth', None)  # To show the full content of columns
print(df[['Product Name', 'Size', 'Price', 'Address', 'Phone']])

df

import pandas as pd
import re

# Load the CSV file
df = pd.read_csv('Pictures/2_ethio_brand_data_cleaned.csv')


import pandas as pd

# Step 1: Read the dataset into a DataFrame (assuming CSV format)
df = pd.read_csv('Pictures/2_ethio_brand_data_cleaned.csv')  # replace with your actual file path

# Step 2: Split the 'Message Text' into multiple columns using string methods
df['Product Name'] = df['Message Text'].str.split('\r\n').str[0]
df['Size'] = df['Message Text'].str.extract(r'size ([\d,]+)')
df['Price'] = df['Message Text'].str.extract(r'price (\d+ birr)')
df['Address'] = df['Message Text'].str.extract(r'አድራሻ-(.*) or call')
df['Phone'] = df['Message Text'].str.extract(r'or call (\d+)')

# Step 3: Update the DataFrame and display it
pd.set_option('display.max_colwidth', None)  # To show the full content of columns
print(df[['Product Name', 'Size', 'Price', 'Address', 'Phone']])

# Optional: Display the first few rows of the entire updated DataFrame
print(df.head())



# Save the cleaned DataFrame to a CSV file
df.to_csv('Pictures/lebeled_ethio_brand_data_cleaned.csv', index=False)

df = pd.read_csv('Pictures/Final_ethio_brand_data_cleaned.csv')


