Python-Practice 4.4.1: Using a hypergeometric distribution.
To find probability, mean,and variance of associated with a hypergeometric distribution, the hypergeom object must be imported from the scipy.stats library. Next, , ,  and  are defined.

from scipy.stats import hypergeom
import matplotlib.pyplot as plt

# Defines the number of successes in the sample, size of the population, number of successes in the population, and size of the sample
k, N, x, n = 12, 52, 26, 20
hypergeom.pmf can be used to calculate the probability of  successes for a given , , and .

# Calculates the probability of k successes given the defined N, x, and n
P = hypergeom.pmf(k, N, x, n, loc=0)
print(P)
0.11975100462360513
hypergeom.cdf gives the cumulative probability of  or fewer successes for a given , , and .

# Calculates the cumulative probability of k or fewer successes
cp = hypergeom.cdf(k, N, x, n)
print(cp)
0.9233198013444432
The mean and variance are calculated using hypergeom.stats.

# Returns the mean of the distribution
mean = hypergeom.stats(N, x, n, loc=0, moments='m')
print(mean)
10.0
# Returns the variance of the distribution
var = hypergeom.stats(N, x, n, loc=0, moments='v')
print(var)
3.1372549019607843
