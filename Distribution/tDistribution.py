Python-Function 4.8.1: t.cdf() and t.sf().
The t.cdf() and t.sf() functions are used to find probabilities related to the -distribution. The scipy.stats library must be imported to use these functions.

t.cdf(t, df, mean, sd) returns the probability of  being less than the critical value  for a -distribution with the specified degrees of freedom, mean, and standard deviation.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t < -0.25)?
print(st.t.cdf(-0.25, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t < 1.5)?
print(st.t.cdf(1.5, 30, 0, 1))
0.40214570454
0.927967035436
t.sf(t, df, mean, sd) returns the probability of  being greater than the critical value  for a -distribution with the specified degrees of freedom, mean, and standard deviation.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t > -0.25)?
print(st.t.sf(-0.25, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t > 1.5)?
print(st.t.sf(1.5, 30, 0, 1))
0.59785429546
0.0720329645643
To find the probability between two critical values, the difference between the two probabilities is calculated.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(-0.25 < t < 1.5)?
print(st.t.cdf(1.5, 30, 0, 1) - st.t.cdf(-0.25, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(1.5 < t < 2.85)?
print(st.t.cdf(2.85, 30, 0, 1) - st.t.cdf(1.5, 30, 0, 1))
0.525821330895
0.0681176765133
Both t.cdf() and t.sf() can also be used for -distributions with different degrees of freedom and when the mean is not  or the standard deviation is not .

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 59, the mean is 55,
# and the standard deviation is 7.5, what is P(t < 62)?
print(st.t.cdf(62, 59, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 34, the mean is 55,
# and the standard deviation is 7.5, what is P(t > 51)?
print(st.t.sf(51, 34, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 59, the mean is 55,
# and the standard deviation is 7.5, what is P(49 < t < 60)?
print(st.t.cdf(60, 59, 55, 7.5) - st.t.cdf(49, 59, 55, 7.5))
0.82277404211
0.701363849613
0.532747974268
