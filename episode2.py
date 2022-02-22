import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/StudentsPerformance.csv", index_col="student_id")
print(df)


# Accessing a single column in a DataFrame
'''
Just as you would access a key-value pair in a dictionary with bracket notation, for example:

two_dimension_data = {
    "gender": ["M","F","M"],
    "first_name": ["John", "Danny", "Andy"],
    "last_name": ["Appleseed", "Bananny", "Davis"],
    "height": [68.24, 70.13, 69.51]
}

print(two_dimension_data["height"]) --> [68.24, 70.13, 69.51]

You can also access a column in a dataframe using bracket notation.
Note, pandas will automatically convert this column into a Series
because it is now one-dimensional

print(df["height"]) --> <Series Object [68.24, 70.13, 69.51]>

A less common but perfectly acceptable alternative is to use dot notation,
as long as your column name doesn't contain spaces/special characters

print(df.height) --> <Series Object [68.24, 70.13, 69.51]>

'''

print(df["math score"])


# Accessing multiple columns in a DataFrame
'''
Instead of just passing in a single column str inside your brackets,
you can pass in a list of column names, creating a "double bracket" effect

df[["student_id", "math score", "reading score", "writing score"]]

Don't be fooled, this is just a list inside bracket notation.
Unfortunately, you cannot access multiple columns using dot notation.

'''

print(df[["math score", "reading score", "writing score"]])


# Accessing Rows
'''
Accessing Rows is done in two ways:
  1. By Position
  
     df.iloc[4] --> goes and gets the row in position 4
     
  2. By Name
  
      df.loc[10000032] --> goes and gets the row under the index with name "10000032"
'''

print(df.iloc[4])
print(df.loc["9610170049"])


# Accessing Rows and columns
'''
df.loc[rows_to_access, columns_to_access]

Use a scalar to access one row/col
Use a list to access multiple rows/cols
Use colon (:) notation to slice out multiple rows/cols

Note: when slicing with .loc the left and right bounds are both inclusive
      when slicing with .iloc only the left bound is inclusive
'''

print(df.loc[10000032, "gender"])
print(df.loc[[10000032,10000034,10000035], ["gender", "telephone"]])
print(df.loc[:, "LUNCH":"writing score"])

print(df.iloc[4, 2])
print(df.iloc[[2,4,7], [2, 0, 6]])
print(df.iloc[3:7, 2:4])


# "Faster" way to access a single data point
print(df.at[10000032, "gender"])
print(df.iat[4, 2])
