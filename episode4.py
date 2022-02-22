import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/StudentsPerformance.csv")
df


# count()
'''
count() counts the number of non NaN/null values in the columns/rows

optional args:
    axis: specifies which axis to count up non-nulls (0 for all the rows, 1 for all the columns)
'''
df.count(axis=1)
df["race/ethnicity"].head(50)


# value_counts()
'''
value_counts() returns the frequency counts of all unique values in the Series

optional args:
    dropna: Don't include counts of NaN values
    normalize: Returns relative frequencies rather than absolute counts
'''

df["race/ethnicity"].value_counts(dropna=False, normalize=True)


# min()
'''
min() returns the minimum value in a Series
'''

df["reading score"].min()


# nsmallest()
'''
nsmallest() returns the smallest n elements in a Series

optional args:
    keep: used to determine whether duplicate values of nth smallest value are included in Series
'''

df["reading score"].nsmallest(3, keep="all")


# max()
'''
max() returns the maximum value in a Series
'''

df["reading score"].max()


# nlargest()
'''
nlargest() returns the largest n elements in a Series

optional args:
    keep: used to determine whether duplicate values of nth largest value are included in Series
'''

df["reading score"].nlargest(3, keep="all")


# mean()
'''
mean() returns the average value in a Series

optional args:
    axis: specifies which axis to take average over (0 for all the rows, 1 for all the columns)
'''

# df["writing score"].mean()
df[["math score", "reading score", "writing score"]].mean(axis=1)


# median()
'''
median() returns the median value in a Series

optional args:
    axis: specifies which axis to take median over (0 for all the rows, 1 for all the columns)
'''

df["writing score"].median()
df[["math score", "reading score", "writing score"]].median(axis=1)


# mode()
'''
mode() returns the mode value in a Series

'''

df["race/ethnicity"].mode()


# std()
'''
std() returns the sample standard deviation in a Series

optional args:
    axis: specifies which axis to take std over (0 for all the rows, 1 for all the columns)
    ddof: delta degrees of freedom
'''

df["writing score"].std()
df[["math score", "reading score", "writing score"]].std(axis=1)


# agg()
'''
agg() returns an aggregate of summary stats

'''

df.agg(["mean", "median", "std"])


# describe()
'''
describe() returns an stats on central tendendy, dispersion, and shape

optional args:
    percentiles: specifies which percentiles to include
'''

df.describe(percentiles=[.2, .4, .6, .8])
