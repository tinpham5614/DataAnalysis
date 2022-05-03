Python-Function 4.9.1: f.cdf() and f.sf().
The f.cdf() and f.sf() functions are used to find probabilities related to the -distribution. The scipy.stats library must be imported to use these functions.

f.cdf(f, dfb, dfw) returns the probability of  being less than a critical value f for an -distribution with  equal to dfb and  equal to dfw.

import scipy.stats as st

# For an F-distribution, if the degrees of freedom between samples is 2
# and the degrees of freedom within samples is 5, what is P(F < 2)?
print(st.f.cdf(2, 2, 5))
0.769951854167
f.sf(f, dfb, dfw) returns the probability of  being greater than a critical value f for an -distribution with  equal to dfb and  equal to dfw.

# For an F-distribution, if the degrees of freedom between samples is 2
# and the degrees of freedom within samples is 5, what is P(F > 3.5)?
print(st.f.sf(3.5, 2, 5))
0.112065490342
To find the probability between two critical values, the difference between the two probabilities is calculated.

# For an F-distribution, if the degrees of freedom between samples is 2
# and the degrees of freedom within samples is 5, what is P(2 < F < 3)?
print(st.f.cdf(3, 2, 5) - st.f.cdf(2, 2, 5))
0.0907506535888
