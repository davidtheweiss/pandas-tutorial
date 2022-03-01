import pandas as pd
from random import randint

students_df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/StudentsPerformance.csv")
print(students_df)

# Create some missing values
for _ in range(50):
    students_df.loc[randint(0,999), "math score"] = None
    
students_df.loc[3, ["math score", "reading score", "writing score"]] = None
students_df.loc[1000] = None
students_df.count()

# isna() filter
'''
Pandas recognizes numpy.NaN as the default "missing", or N/A, value.
The method isna() is great for filtering for values labeled NaN in your DataFrame.
Running isna() returns a Series of bools indicating where missing values are located

If you perfer, you can use isnull() instead, they work the exact same!
'''

filt = students_df["math score"].isna()
students_df[filt]

# notna() filter
'''
The method notna() is great for filtering out values labeled NaN in your DataFrame.
Running notna() returns a Series of bools indicating where non-empty values are located

If you perfer, you can use notnull() instead, they work the exact same!
'''

filt = students_df["math score"].notna()
students_df[filt]

# dropna()
'''
If you have missing data in your dataframe, one approach for handling
it is to just remove the row/column it lives in.

    students_df.dropna(axis=0, how="any", thresh=0, subset=[], inplace=False)
'''

students_df.dropna(thresh=9)

# fillna()
'''
A different approach to handling missing data is to fill
NaNs with a different value

    students_df.fillna(value=None, method=None, axis=None, inplace=False, limit=None)
    
Extra Credit: you can also use the method: interpolate().
This will use a procedure known as interpolation to fill
in the gaps between data points.

    students_df.interpolate(method="linear")
'''

students_df.loc[1:2, ["math score", "reading score", "writing score"]] = None
students_df.fillna(method="ffill", limit=2)
students_df["race/ethnicity"].fillna("Not Specified").value_counts()

students_df.interpolate(method="quadratic")
