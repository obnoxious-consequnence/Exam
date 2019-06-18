import pandas as pd
df1 = pd.read_csv("https://pythonhow.com/data/income_data.csv")
df2 = df1.set_index("State", drop=False)
# Instead of getting an auto-generated index, we set it states
# drop: Delete columns to be used as the new index.

# Extracting a subset of a pandas dataframe
df2.loc["Alaska":"Arkansas", "2005":"2007"]
# This will print everything from

# Extracting a column of a pandas dataframe
df2.loc[:, "2005"]
df2["2005"]

# Extracting a row of a pandas dataframe
df2.loc["California", :]

# Extracting specific columns of a pandas dataframe
df2[["2005", "2008", "2009"]]

# Extracting specific rows of a pandas dataframe
df2[1:3]

# Extracting a single cell from a pandas dataframe
df2.loc["California", "2013"]

# Position based indexing
df2.iloc[0:3, 0:4]
# df2.ix[0:3, "2005":"2007"]

print(df2)
print(df2.loc[:, "2005"].mean())
