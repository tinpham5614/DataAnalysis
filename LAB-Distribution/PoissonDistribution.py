import numpy as np
from scipy.stats import poisson
# import the correct module and function

x = int(input())
lam = int(input())

np.random.seed(seed=123)

# Generate 8 random numbers with a Poisson distribution with a mean of lam
r1 = poisson.rvs(lam, size=8)# Code for generating distribution

# Generate 20 random numbers with a Poisson distribution with a mean of lam
r2 = poisson.rvs(lam,size=20)# Code for generating distribution

# Generate 100 random numbers with a Poisson distribution with a mean of lam
r3 = poisson.rvs(lam,size=100)# Code for generating distribution

# Calculate the cumulative probability of x or fewer successes for a Poisson distribution with a mean of lam
cp = poisson.cdf(x, lam)# Code for cumulative probability
print("Cumulative probability is ",cp)

# Calculate the theoretical mean of the Poisson distribution
mean_theor = poisson.stats(lam, moments='m')# Code for theoretical mean
print("Theoretical mean is ", mean_theor)

# Calculate the actual mean of r1, r2, and r3
mean_r1 = poisson.stats(sum(r1)/8, moments='m')# Code for actual mean of r1
print("Mean of r1 is ", mean_r1)

mean_r2 = poisson.stats(sum(r2)/20, moments='m')# Code for actual mean of r2
print("Mean of r2 is ", mean_r2)

mean_r3 = poisson.stats(sum(r3)/100, moments='m')# Code for actual mean of r3
print("Mean of r3 is ", mean_r3)
