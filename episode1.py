import pandas as pd


# Pandas Series
'''
Tabular data is often two-dimensional, there are multiple columns and rows in the dataset.
However, pandas has a special data type for one-dimensional data, known as Series.
Series are kind of like a single column of your data set.
You can think of a Series like the pandas equivalent of a python list,
while a dataframe is like the pandas equivalent of a 2D python dictionary (with keys as cols and values as rows).

pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)

'''
one_dimension_data = [32.46, 23.75, 27.1, 90.62, 74.74] # list
one_dimension_data = (32.46, 23.75, 27.1, 90.62, 74.74) # tuple
one_dimension_data = 41 # scalar (int)
one_dimension_data = "David" # scalar (str)
one_dimension_data = {'row1': 32.46, 'row2': 23.75, 'row3': 27.1} # 1D dictionary
one_dimension_data = (i for i in range(10)) # generator

ds = pd.Series(one_dimension_data, name="heights")
print(ds)


# Pandas Dataframe
'''
Data loaded in pandas with more than one column is known as a DataFrame.
This is the primary data structure in pandas, as most datasets have more than one column

pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)

'''
two_dimension_data = {
    "gender": ["M","F","M"],
    "first_name": ["John", "Danny", "Andy"],
    "last_name": ["Appleseed", "Bananny", "Davis"],
    "height": [68.24, 70.13, 69.51]
}

df = pd.DataFrame(two_dimension_data)
print(df)


# Pandas Read CSV
# sep & usecols optional args
df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/livingwage.tsv", sep='\t')
print(df)

pd.set_option('display.max_columns', 1000)
print(df)


print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
