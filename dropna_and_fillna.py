# Import the necessary modules
import pandas as pd

hmeq = pd.read_csv('hmeq_small.csv') # Code to read in hmeq_small.csv

# Create a new data frame with the rows with missing values dropped
df1 = (hmeq.dropna())# Code to delete rows with missing values

# Create a new data frame with the missing values filled in by the mean of the column
df2 = (hmeq.fillna(hmeq.mean())) # Code to fill in missing values

# Print the means of the columns for each new data frame
print("Means for df1 are ", df1.mean()) # Code to find means of df1

print("Means for df2 are ", df2.mean()) # Code to find means of df2
