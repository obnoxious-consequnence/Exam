import pandas as pd
df1 = pd.read_csv("https://pythonhow.com/data/income_data.csv")
df2 = df1.set_index("State")

df2.loc[:, "2005":"2010"]
