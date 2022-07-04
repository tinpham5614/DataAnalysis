Python-Function 4.7.2: norm.ppf() and norm.isf().
The norm.ppf() and norm.isf() functions are used to convert percentiles to -scores. The scipy.stats library must be imported to use these functions.

norm.ppf(p, mean, sd) returns the critical -score for which the probability of  being below that -score is p, for a normal distribution with the specified mean and standard deviation.

import scipy.stats as st

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is z* if P(z < z*) = 0.135?
print(st.norm.ppf(0.135, 0, 1))
-1.1030625562
norm.isf(p, mean, sd) returns the critical -score for which the probability of  being above that -score is p, for a normal distribution with the specified mean and standard deviation.

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is z* if P(z > z*) = 0.405?
print(st.norm.isf(0.405, 0, 1))
0.240426031142
Both norm.ppf() and norm.isf() can also be used with non-standard normal distributions.

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is x* if P(x < x*) = 0.8247?
print(st.norm.ppf(0.8247, 55, 7.5))

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is x* if P(x > x*) = 0.95?
print(st.norm.isf(0.95, 55, 7.5))
62.0006958915
42.6635977979
