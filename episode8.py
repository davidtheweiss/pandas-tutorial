import pandas as pd

students_df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/StudentsPerformance.csv")
print(students_df)


# groupby()
'''
groupby() is helpful when you want to split up your dataframe
by common values in one or more of the columns of your dataset.
Then, once common values are grouped together, you can apply some
aggregation function on it.

Performs a "GROUP BY" operation similar to SQL.

    df.groupby(by=None, sort=True, dropna=True, as_index=True)
'''

# So far all we know how to do is apply a function on the entire column
students_df["math score"].mean()

# Simply applying groupby creates a "GroupBy object"
students_df.groupby("race/ethnicity")

# Have a look at the groups and their matched rows
students_df.groupby("race/ethnicity").ngroups
students_df.groupby("race/ethnicity").groups
students_df.groupby("race/ethnicity").first()
students_df.groupby("race/ethnicity").get_group("african american")

# Apply an aggregation function on dataframe/column based on groups
students_df.groupby("race/ethnicity").mean()
students_df.groupby("race/ethnicity", sort=False, dropna=False)["math score"].mean()

# You can group by multiple columns
students_df.groupby(["race/ethnicity", "test preparation course"], as_index=False)["math score"].mean()
