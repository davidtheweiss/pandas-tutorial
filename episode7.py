import pandas as pd

students_df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/StudentsPerformance.csv")
print(students_df)


# replace()
'''
Replaces values in dataframe/series with another piece of data you specify.
You can lookup values to replace by exact match or regular expression.
This method can be used on dataframes, series, or a str method (str.replace)

    ds.replace(to_replace=None, value=NoDefault.no_default, inplace=False,
               limit=None, regex=False, method=NoDefault.no_default)
'''

students_df["test preparation course"].value_counts()
students_df["test preparation course"].replace("none", False)

filt = students_df["telephone"].str.len() == 10
students_df[~filt]

students_df["telephone"].replace("(\+1|[()\-\s])", "", regex=True)[~filt]


# apply()
'''
The method apply() is often used when you want to pass your Series through a
custom transformation function. While there are numerous pre-built methods for
common transformations into pandas, it's impossible to cover every single edge case.
apply() fills in the gaps.

    ds.apply(custom_function, axis=0)

apply() will pass every value of the Series into the custome function as an argument
'''

# Custom function performed on Series data
def calc_letter_grade(value):
    if value >= 90:
        return "A"
    elif value >= 80:
        return "B"
    elif value >= 70:
        return "C"
    elif value >= 60:
        return "D"
    else:
        return "F"

students_df["math_grade"] = students_df["math score"].apply(calc_letter_grade)
students_df

# Using apply accross columns
def calc_composite_score(row):
    return (row["math score"] + row["reading score"] + row["writing score"]) / 3

students_df["composite score"] = students_df[["math score", "reading score", "writing score"]].apply(calc_composite_score, axis=1)
students_df

# Some simple transformations can be accomplished using operators
students_df.LUNCH + " lunch"

# Feel free to pass in existing "built-in" functions to apply :)
students_df["writing score"] = students_df["writing score"].apply(abs)
students_df


# applymap()
'''
Similar to how apply() applies a custom function element-wise for Series,
applymap() applies a custom function element-wise for DataFrames

    applymap(func, na_action)
'''

def redact(value):
    return len(str(value)) * '*'

students_df.applymap(redact)

# Using lambdas (often used in applymap() & apply()!)
students_df[["math score", "reading score", "writing score"]].applymap(lambda val: val / 100)


# drop()
'''
Removes columns/rows from your DataFrame/Series

    drop(columns=None, index=None, inplace=False, errors='raise')
'''

# dropping columns
students_df.drop(columns=["telephone", "math_grade"])

# dropping rows (can be explicit which indicies to drop or based on filter!)
filt = students_df["math score"] < 70
filtered_df = students_df[filt]
filtered_df

students_df.drop(index=filtered_df.index)
