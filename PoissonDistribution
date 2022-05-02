Python-Practice 4.5.1: Using a Poisson distribution.
To find probability, mean,and variance of associated with a Poisson distribution, the poisson object must be imported from the scipy.stats library. Next,  is defined.

from scipy.stats import poisson

# Defines the desired number of successes and the mean of the distribution
x, lam= 12, 9
poisson.pmf can be used to calculate the probability of  successes for a given .

# Calculates the probability of x successes given the defined lambda
P = poisson.pmf(x, lam)
print(P)
0.0727650466416229
poisson.cdf gives the cumulative probability of  or fewer successes for a given .

# Calculates the cumulative probability of x or fewer successes given the defined lambda
cp = poisson.cdf(x, lam)
print(cp)
0.8757734291709649
The mean and variance are calculated using poisson.stats.

# Returns the mean of the distribution
mean = poisson.stats(lam, moments='m')
print(mean)
9.0
# Returns the variance of the distribution 
var = poisson.stats(lam, moments='v')
print(var)
9.0
poisson.rvs can be used to generate a set of random numbers with the Poisson distribution defined by .

# Generates 10 random numbers with a Poisson distribution with a mean of lam
r = poisson.rvs(lam, size=10)
print(r)
[ 7  7 11 14  9  5  9  9 12 10]
