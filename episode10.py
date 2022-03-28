import pandas as pd

students_df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/StudentsPerformance.csv")
print(students_df)


# rename
"""
Used for renaming the column and index names

    df.rename(mapper, index=None, columns=None, axis=None, inplace=False)
"""

# Replace exact matches
students_df.rename({"LUNCH": "lunch", "student_id": "id"}, axis=1)
students_df.rename(columns={"LUNCH": "lunch", "student_id": "id"})
students_df.rename(index={2: "row_2", 996: "row_996"})

# Replace using a custom function
def camel_caseify(col_name):
    return col_name[0].lower() + ''.join(x for x in col_name.title() if x.isalpha())[1:]

students_df.rename(camel_caseify, axis=1)


# str.replace
"""
An alternative way to rename columns

    df.columns.str.replace(pat, repl, regex=None)
"""

students_df.columns = students_df.columns.str.replace("\s", "_", regex=True)
students_df.math_score


# set_index
"""
Sets the index of your dataframe using an existing column

    df.set_index(keys, verify_integrity=False, inplace=False)
"""

# Define which column(s) should be used as index
students_df.set_index("student_id")

# ensure no two indicies are the same
students_df.set_index("math_score", verify_integrity=True)

students_df.set_index("student_id", inplace=True)
students_df


# reset_index
"""
Transforms indicies into a regular table column
and reverts indicies back to range.
This is basically the opposite of set_index()

    df.reset_index(drop=False, inplace=False)
"""

# Convert indicies back to range and create new column with previous indicies
students_df.reset_index()

# Convert indicies back to range and delete previous indicies
students_df.reset_index(drop=True)
