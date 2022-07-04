Python-Practice 4.3.1: Using a binomial distribution.
To find probability, mean,and variance associated with a binomial distribution, the binom object must be imported from the scipy.stats library. Next, , , and  are defined.

from scipy.stats import binom

# Defines the number of successes, the number of trials, and the probability of a success in each trial
k, n, p = 5,10, 0.7
binom.pmf can be used to calculate the probability of  successes for a given  and .

# Calculates the probability of k successes given the defined n and p
P = binom.pmf(k, n, p)
print(P)
0.10291934520000011
binom.cdf gives the cumulative probability of  or fewer successes for a given  and .

# Calculates the cumulative probability of k or fewer successes
cp = binom.cdf(k, n, p)
print(cp)
0.15026833260000008
The mean and variance are calculated using binom.stats.

# Returns the mean of the distribution
mean  =  binom.stats(n, p, moments = 'm')
print(mean)
7.0
# Returns the variance of the distribution 
var = binom.stats(n, p, moments='v')
print(var)
2.1000000000000005
