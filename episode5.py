import pandas as pd
from random import randint

students_df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/StudentsPerformance.csv")
print(students_df)

colleges_df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/Colleges.csv")
print(colleges_df)

# Adding a column(s) to a dataframe
'''
There are many quick ways you can add a new column to your dataframe through assignment:

    1. Assigning a new Series to a scalar will give every value of that column the same value
    2. Assigning a new Series to a list will convert that list to a Series
    3. Assigning a new Series to an existing Series
    4. You can also assign multiple columns at once!

The syntax works like this:
    
    students_df["name of new or existing column"] = new_values(s)
    
You can also use the insert method to define where you want your column positionally,
and protect against overwritting existing columns

    students_df.insert(location, column_name, value, allow_duplicates=False)
    
'''

students_df["date_of_exam"] = '02/22/22'
students_df["experiment_group"] = [("group A", "group B", "group C")[randint(0, 2)] for _ in range(students_df.shape[0])]
students_df["experiment_group_copy"] = students_df["experiment_group"]
students_df[["country_of_residence", "state_of_residence"]] = ["USA", "California"]

students_df.insert(3, "high school", "Ridgemount High", allow_duplicates=True)
students_df

# Adding a row to a dataframe
'''
Using the same logic as above, you can also add rows through assignment.
However, you must use .loc as .iloc is not allowed

    colleges_df.loc[index_name] = ["10007", "Stanford", "Stanford, CA"]
    colleges_df.loc[index_name] = "A Single Value to be repeated for every column"
    
'''

colleges_df.loc[8] = ["10008", "Stanford", "Stanford, CA"]
colleges_df

# Appending Dataframes
'''
Most often, when adding new rows to a dataframe, you'll want
to combine two dataframes. This is called appending.
    
    df.append(df2, ignore_index=False)
    
'''

more_colleges = pd.DataFrame([
    [10009, "Duke", "Durham, NC"],
    [10010, "Cal Tech", "Pasadena, CA"],
    [10011, "MIT", "Cambridge, MA"],
    [10012, "Oxford", "Oxford, UK"]
], columns=["id", "name", "location"])

# NOTE: This method is deprecated as of v1.4.0, but you still may see it in the wild
aggregate_colleges_df = colleges_df.append(more_colleges, ignore_index=True)
aggregate_colleges_df

# Concatenating Dataframes
'''
Using pandas concat method is much more versatile, as it
can combine Series/DataFrame both vertically and horizontally
    
    pd.concat([df1, df2], axis=0, ignore_index=False)
    
'''

concat_df = pd.concat([colleges_df, more_colleges], axis=1)
concat_df

# Merging Dataframes
'''
The merge function mimics relational database style JOINs.
You can specify inner, outer, left, right and cross joins
on two related columns/indexes from different dataframes
    
    pd.merge(df1, df2, how="inner",
             on=None, left_on=None, right_on=None,
             left_index=False, right_index=False, indicator=False)
    
'''

merged_df = pd.merge(students_df, colleges_df, left_index=True, right_index=True, how="left", indicator="Data Live In")
merged_df.head(30)

# Joining Dataframes
'''
While less common than merge, pandas supports a second
way of joining two dataframes together on a common index/column.
This method is less versatile than merge, but it does exist,
so it's important to at least recognize what it does

    df.join(df2, how="left", on=None, lsuffix="", rsuffix="")
    
'''

joined_df = students_df.join(colleges_df.set_index("id"), on="college_id")
joined_df
