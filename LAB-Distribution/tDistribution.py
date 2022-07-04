# The United States Census Bureau determined that the mean number of children in an American household is 1.86.
# Suppose 50 households are polled and the sample mean is found to be 2.1 and the standard deviation is found to be 1.57.
# Write a program that finds the probability that another 50 household sample will have a sample mean of at least 2.1.
# The output should be:
# The probability that another 50 household sample will have a sample mean of at least 2.1 is 0.14251039487167508.

import scipy.stats as st
import math
from cmath import sqrt
# the math package is necessary because the expression for t uses the math.sqrt(x) function.

n = 50# what is the sample size?
pop_mean = 1.86# what is the population mean?
sam_mean = 2.1# what is the sample mean?
sd = 1.57# what is the standard deviation?
df = 49# what is the degrees of freedom?

t = (sam_mean - pop_mean) / (sd/(math.sqrt(n)))# write an expression to find the value of t. 

prob = st.t.sf(t, df, 0, 1) # use the st.t.sf function to find the probability

print("The probability that another 50 household sample will have a sample mean of at least 2.1 is " + str(prob) + ".")
