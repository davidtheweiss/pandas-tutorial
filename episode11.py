import pandas as pd

students_df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/StudentsPerformance.csv")
students_df


# sort_values()
"""
Sorts a Dataframe/Series by its values
in a given column(s) or row(s).

    df.sort_values(by, axis=0, ascending=True, inplace=False, key=None)
    
The "by" argument can be a scalar or a list.
If it's a list, the first element will be
sorted first, and if their is a tie, the second
element will be the tiebreaker.
"""

# Sort by a single column
students_df.sort_values(by="math score", ascending=False)

# Sort by multiple columns
students_df.sort_values(by=["math score", "reading score"], ascending=False)

# Sort with custom function
students_df.sort_values(by="parental level of education", key=lambda ds: ds.apply(len))


# sort_index()
"""
Sorts a Dataframe/Series by its indicies

    df.sort_index(axis=0, ascending=True, inplace=False, key=None)
"""

# Sort by index
students_df.set_index("college_id").sort_index()


# nlargest() & nsmallest()
"""
Displays the n largest/smallest values in
a column

    df.nlargest(n, columns, keep="first")
    df.nsmallest(n, columns, keep="first")
"""

# Get the n largest values
students_df.nlargest(10, columns="math score")

# Get the n smallest values
students_df.nsmallest(10, columns="math score")
