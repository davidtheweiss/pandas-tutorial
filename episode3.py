import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/StudentsPerformance.csv")
print(df)


# Accessing rows that pass a filter
'''
You can pass in the column name or row positions into bracket notation

E.g.
    df["math score"] --> gets data in column "math score"
    df[5:30] --> gets data in rows 5 through 29

But you can also filter rows by passing in a filter

    filt = (df["gender"] == "male")
    df[filt] --> gets all rows where gender is equal to "male"
'''

filt = (df["gender"] == "male")
df[filt]


# You can also pass in a filt to .loc[] but NOT .iloc[]
'''
Passing in a filt through .loc[] provides more flexibility
because you can also specify columns to access

    df.loc[filt, ["gender", "math score", "reading score", "writing score"]]

'''

filt = (df["gender"] == "male")
df.loc[filt, ["gender", "math score", "reading score", "writing score"]]


# Common filter operators
'''
    == --> equal to
    & --> and
    | --> or
    ~ --> not
'''

# Gender is "male" and race/ethnicity is "asian american"
filt = (df["gender"] == "male") & (df["race/ethnicity"] == "asian american")
df[filt]

# Math score is greater than or equal to 85 and reading score is greater than 80
filt = (df["math score"] >= 85) | (df["reading score"] > 80)
df[filt]

# Parental level of education is not high school
filt = ~(df["parental level of education"] == "high school")
df[filt]


# More complicated filter expressions
'''
    isin() --> checks to see whether value is in list
    str.contains() --> checks whether string contains a substring
    str.len() --> gets string's length
'''

# Parental level of education is either BA, AD, or some college
filt = (df["parental level of education"].isin(["bachelor's degree", "associate's degree", "some college"]))
df[filt]

# LUNCH has the word "free" in it
filt = (df["LUNCH"].str.contains("free"))
df[filt]

# Telephone has more than 10 characters
filt = (df["telephone"].str.len() > 10)
df[filt]
