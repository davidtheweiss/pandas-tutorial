import pandas as pd

df = pd.read_csv("/Users/David/Desktop/pandas_tutorial/StudentsPerformance.csv")
pd.set_option('display.max_columns', 10)

print(df)
