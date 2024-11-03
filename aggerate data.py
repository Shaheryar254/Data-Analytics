# Finding maximum
maxvalue = df["value_eur"].max()
print(maxvalue)

# You can find the row location of the maximum value with idxmax()

#Finding minimum
minvalue = df["value_eur"].min()
print(minvalue)

# same thing with idxmin

#Finding the total
print("total wages in fifa is", df["wage_eur"].sum())

#Finding the average mode and median
""" .mean()
    .mode()
    .median()
"""

#To analysises the whole dataframe
print(df.describe())
