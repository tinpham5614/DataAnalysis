Python-Function 4.8.2: t.ppf() and t.isf().
The t.ppf() and t.isf() functions are used to convert percentiles to -statistics. The scipy.stats library must be imported to use these functions.

t.ppf(p, df, mean, sd) returns the critical -statistic for which the probability of  being below that -score is p, for a -distribution with the specified degrees of freedom, mean, and standard deviation.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 49, the mean is 0 and 
# the standard deviation is 1, what is t* if P(t < t*) = 0.135?
print(st.t.ppf(0.135, 49, 0, 1))
-1.11568202664
t.isf(p, df, mean, sd) returns the critical -statistic for which the probability of  being above that -score is p, for a -distribution with the specified degrees of freedom, mean, and standard deviation.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 49, the mean is 0 and 
# the standard deviation is 1, what is t* if P(t > t*) = 0.405?
print(st.t.isf(0.405, 49, 0, 1))
0.241727638106
Both t.ppf() and t.isf() can also be used with non-standard -distributions.

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 24, the mean is 55 and 
# the standard deviation is 7.5, what is t* if P(t < t*) = 0.8247?
print(st.t.ppf(0.8247, 24, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 24, the mean is 55 and 
# the standard deviation is 7.5, what is t* if P(t > t*) = 0.95?
print(st.t.isf(0.95, 24, 55, 7.5))
62.1398037924
42.1683844007
