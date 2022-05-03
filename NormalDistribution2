Python-Function 4.7.1: norm.cdf() and norm.sf().
The norm.cdf() and norm.sf() functions are used to find probabilities related to the normal distribution. The scipy.stats library must be imported to use these functions.

norm.cdf(z, mean, sd) returns the probability of  being less or equal to than the critical value  for a normal distribution with the specified mean and standard deviation.

import scipy.stats as st

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z <= -0.25)?
print(st.norm.cdf(-0.25, 0, 1))

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z <= 1.5)?
print(st.norm.cdf(1.5, 0, 1))
0.401293674317
0.933192798731
norm.sf(z, mean, sd) returns the probability of  being greater than or equal to the critical value  for a normal distribution with the specified mean and standard deviation.

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z >= -0.25)?
print(st.norm.sf(-0.25, 0, 1))

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z >= 1.5)?
print(st.norm.sf(1.5, 0, 1))
0.598706325683
0.0668072012689
To find the probability between two critical values, the difference between the two probabilities is calculated.

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(-0.25 <= z <= 1.5)?
print(st.norm.cdf(1.5, 0, 1) - st.norm.cdf(-0.25, 0, 1))

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(1.5 <= z <= 2.85)?
print(st.norm.cdf(2.85, 0, 1) - st.norm.cdf(1.5, 0, 1))
0.531899124414
0.0646212398139
Both norm.cdf() and norm.sf() can also be used for non-standard normal distributions, that is, when the mean is not  or the standard deviation is not .

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is P(x <= 62)?
print(st.norm.cdf(62, 55, 7.5))

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is P(x >= 51)?
print(st.norm.sf(51, 55, 7.5))

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is P(49 <= x <= 60)?
print(st.norm.cdf(60, 55, 7.5) - st.norm.cdf(49, 55, 7.5))
0.824676055148
0.703098571396
0.53565206387
