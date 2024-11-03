
germanAge = df.loc[(df['nationality_name'] 'Germany'), ['short_name', 'club_name', 'player_positions', 'pace']]
print(germanAge__Pos.dropna()) # Adding the .dropna() will remove empty data

print(df["age"].drop_duplicates()) # adding the drop_duplicates() will remove any duplicated values

# Changing columns data type

print(df["short_name"]) # printing the column will show the data type at the bottom

# converting float to str
print(df["value_eur"].astype("str"))

# if you are using pandas
print(df.loc[df['overall'] > 88, ['short_name', 'club_name', 'overall']].to_string()) # the to_string will do it

#int to float
print(df["wage_eur"].dropna().astype("int")) # the dropna also gets rid of null values

#to convert data frame we need to use dictionaires
print(dict(df["short_name"][:10]))

"""to access items in the dictionary
store the dictionary as a variable"""
datadict = dict(df["short_name"][:10])
# loop through the items in it (key/value)
for index, value in datadict.items():
    print(index, "is", value)
print(list(df["value_eur"][:10]))












