# Import the necessary modules
import pandas as pd
from sklearn import preprocessing
import numpy as np
hmeq = pd.read_csv('hmeq_small.csv') # Read in the file hmeq_small.csv

# Standardize the data
standardized = preprocessing.scale(hmeq) # Code to standardize the data

# Output the standardized data as a data frame
df1 = pd.DataFrame(standardized, columns = ["LOAN", "MORTDUE", "VALUE", "YOJ", "CLAGE", "CLNO", "DEBTINC"]) # Code to output as a data frame

# Normalize the data
normalized = preprocessing.MinMaxScaler().fit_transform(hmeq) # Code to normalize the data

# Output the standardized data as a data frame
df2 = pd.DataFrame(normalized, columns = ["LOAN", "MORTDUE", "VALUE", "YOJ", "CLAGE", "CLNO", "DEBTINC"]) # Code to ouput as a data frame

# Print the means and standard deviations of df1 and df2
print("The means of df1 are ", df1.mean()) # Code for mean of df1
print("The standard deviations of df1 are ", df1.std()) # Code for standard deviation of df1
print("The means of df2 are ", df2.mean()) # Code for mean of df2
print("The standard deviations of df2 are ", df2.std()) # Code for standard deviation of df2
