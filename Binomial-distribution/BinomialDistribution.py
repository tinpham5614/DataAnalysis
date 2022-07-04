# Given a fair coin flipped 100 times, find the probability of a user-defined number of flips coming up heads.
# Find the mean and variance of the binomial distribution.

# Ex: When the input is:
# 27

# the output is:
# 1.51252E-06
# 50.00
# 25.00


# Load the necessary module
from scipy.stats import binom
# Get user-defined number of successes
k = int(input())

# Set the number of trials and the probability of success in each trial
n, p = 100, 0.5
# Calculate the probability of k successes given the defined n and p
P =  binom.pmf(k, n, p)# Code to calculate probability
print(f'{P:.5E}')

# Return the mean of the distribution
mean  =  binom.stats(n, p, moments = 'm')# Code to find mean
print(f'{mean:.2f}')

# Return the variance of the distribution 
var = binom.stats(n, p, moments='v')# Code to find variance
print(f'{var:.2f}')
