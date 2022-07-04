Python-Practice 4.10.1: Finding areas and percentiles.
To find the area under a chi-square distribution or the  at which the distribution has a given area, the chi2 object must be imported from the scipy.stats library. Next, the degrees of freedom and  are defined.

from scipy.stats import chi2

# Defines the degrees of freedom and chi-square_0
df = 7
x2 =  1.689
chi2.cdf can be used to calculate the area under the curve between  and .

# Calculates the area under the curve between 0 and chi-square_0
area = chi2.cdf(x2, df)

print(area)
0.02496315095256541
Conversely, if the area is defined, chi2.ppf gives the  value, or percentile, necessary to obtain that area.

# Defines an area under the curve

a = 0.025

# Calculates the percentile
perc = chi2.ppf(a, df)

print(perc)
1.6898691806773554

-------------------------------------------

Example 4.10.3: Finding probability.
A company makes LED light bulbs with a stated life expectancy of  hours. The standard deviation is  hours. A customer buys  bulbs and finds a standard deviation of  hours. If the customer bought  more bulbs, what is the probability that the standard deviation of the new sample would be less than  hours?

Solution
As shown in the example above, the chi-square statistic for this situation is . To find the probability that the standard deviation of a new sample of  bulbs would be less than  hours,  and  can be entered into statistical software.

from scipy.stats import chi2

df = 7
x2 = 3.111

area = chi2.cdf(x2, df)

print(area)
0.12545259857860666
Thus the probability is  that the standard deviation of another sample of  LED bulbs will be less than  hours.

-------------------------------------------

Example 4.10.4: Finding percentiles.
What is the th percentile of a chi-square distribution with  degrees of freedom?

Solution
The th percentile is the  value at which the volume under the chi-square curve is . This value can be found using statistical software with  and .

from scipy.stats import chi2

df = 5
a = 0.95

perc = chi2.ppf(a, df)

print(perc)
11.070497693516351
Thus, the  value that marks the th percentile for a chi-square distribution with  degrees of freedom is .
