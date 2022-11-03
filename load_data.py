# Dependency needed to install file 

# pip install xlrd

# Import required library

import pandas as pd

# Read data from CSV file

# first we define the data path as csv_path
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path) # now we create a dataframe called df using the read_csv pandas method and calling csv_path as arg

# Print first five rows of the dataframe

print(df.head()) # blank paranthesis shows first 5 rows of df
# df.head(2) # value in parenthesis shows value # of rows in df

# Read data from Excel File and print the first five rows

# first define excel file path
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

# use pandas "read_excel" method with xlsx_path arg
df = pd.read_excel(xlsx_path)
df.head() # print first 5 rows of df

# this code block produces an error as of 2 Jan 2022. Looks like pip is needed to install openpxyl but this is already performed earlier in lab w/ success 

# Access to the column Length

x = df[['Length']] # defining x as a pandas dataframe consisting of only the Length column from dataframe "df"
x
# type(x)

# Get the column as a series

x = df['Length'] # only using one bracket returns x as a pandas series
x
#type(x)

# Get the column as a dataframe

x = df[['Artist']]
x
#type(x)

# Access to multiple columns

y = df[['Artist','Length','Genre']]
y
#type(y)

# Access the value on the first row and the first column

df.iloc[0, 0]

# Access the value on the second row and the first column

df.iloc[1,0]

# Access the value on the first row and the third column

df.iloc[0,2]

# Access the value on the second row and the third column
df.iloc[1,2]

# Access the column using the name

df.loc[1, 'Artist']

# Access the column using the name

df.loc[1, 'Artist']

# Access the column using the name

df.loc[0, 'Released']

# Access the column using the name

df.loc[1, 'Released']

# Slicing the dataframe

df.iloc[0:2, 0:3]

# Slicing the dataframe using name

df.loc[0:2, 'Artist':'Released']

q = df[['Rating']]

q = df[['Released','Artist']]

df.iloc[1,2]

# the following list to convert the dataframe index df to characters and assign it to df_new; find the element corresponding to the row index a /
# and column 'Artist'. Then select the rows a through d for the column 'Artist'

new_index=['a','b','c','d','e','f','g','h']

df_new=df   # define df_new as df, creating a new variabe to work with
df_new.index = new_index  #  this casts the elements of the 'new_index' list as index values for the df_new dataframe
df_new.loc['a','Artist']   # element at 'a' and 'Arist'... note the 'loc' method inputs string values. I think the 'iloc' method uses values only as args
df_new.iloc[0,2]

