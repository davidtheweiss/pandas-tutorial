"""
If you aren't using jupyter and running this in a normal
python IDE, you'll have to use matplotlib.pyplot interface
to see your plots!

    pip3 install matplotlib
    
    import matplotlib.pyplot as plt
    plt.show()  # at the end of your code!
"""
import pandas as pd


students_df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/StudentsPerformance.csv")
print(students_df)

cpi_df = pd.read_csv("https://raw.githubusercontent.com/davidtheweiss/pandas-tutorial/main/CPILFESL.csv")
print(cpi_df)

# plot
"""
Plots your dataframe/series on a graph, allowing
for deeper understanding through data visualization.

    df.plot(x=None, y=None, kind="line", figsize=None)
"""

# All it takes to see a nice graph is .plot()
cpi_df.plot()

# Specify the data for the x- and y-axis
cpi_df.plot(x="DATE", y="CPILFESL")

# Lets clean up our plot a little bit
cpi_df.plot(x="DATE"); # Add a semicolon to hide IPython text output
cpi_df.plot(x="DATE", figsize=(15, 6)); # change display size (width, height) in inches
cpi_df.plot( # Add title and axis labels
    x="DATE",
    y="CPILFESL",
    title="Consumer Price Index for All Urban Consumers: All Items Less Food and Energy in U.S. City Average",
    label="USA",
    xlabel="Date",
    ylabel="CPI (without food & energy)",
    figsize=(15, 6)
);
cpi_df.plot( # Formatting your graph
    x="DATE",
    y="CPILFESL",
    title="Consumer Price Index for All Urban Consumers: All Items Less Food and Energy in U.S. City Average",
    label="USA",
    xlabel="Date",
    ylabel="CPI (without food & energy)",
    figsize=(15, 6),
    linewidth=4,
    color="#DC1C13",
    legend=False,
    grid=True,
    fontsize=13
);

# lets add a regression line (optional)
import numpy as np  # pip install numpy
b2, b1, b0 = np.polyfit(cpi_df.index, cpi_df.CPILFESL, deg=2)
cpi_df["regression line"] = [b0 + (b1 * x) + (b2 * x ** 2) for x in cpi_df.index]
cpi_df.plot()

# types of plots
"""
line: line plot (default)
bar: vertical bar plot
barh: horizontal bar plot
hist: histogram
box: boxplot
kde: Kernel Density Estimation plot
density: same as ‘kde’
area: area plot
pie: pie plot
scatter: scatter plot (DataFrame only)
hexbin: hexbin plot (DataFrame only)
"""

# plots a line graph by default
students_df.plot(x="math score", y="reading score");

# scatter
students_df.plot(x="math score", y="reading score", kind="scatter");
students_df.plot.scatter(x="math score", y="reading score");

# bar
students_df.groupby("gender")["reading score"].mean().plot(kind="bar");
students_df.groupby("gender")["reading score"].mean().plot.bar();

# histogram
students_df.plot(y="math score", kind="hist");
students_df.plot.hist(y="math score");

# pie
students_df.groupby("race/ethnicity")["student_id"].count().plot(kind="pie");
students_df.groupby("race/ethnicity")["student_id"].count().plot.pie();
