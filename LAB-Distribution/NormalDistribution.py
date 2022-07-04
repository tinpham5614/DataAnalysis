# The normalized distribution for a person's intelligence quotient (IQ) has a mean of 100 and a standard deviation of 15. 
# Write a program that takes two values for IQ (IQ1 and IQ2) as inputs and calculates the following probabilities for a randomly selected person having an IQ:

# greater than or equal to IQ1
# less than or equal to IQ1
# between IQ1 and IQ2

# import scipy.stats
import scipy.stats as st

# input two IQs, making sure that IQ1 is less than IQ2
IQ1 = float(input())
IQ2 = float(input())

while IQ1 > IQ2:
    print("IQ1 should be less than IQ2. Enter numbers again.")
    IQ1 = float(input())
    IQ2 = float(input())

prob_al = st.norm.sf(IQ1,100,15) # write a command that calculates the probability that a randomly
          # selected person has is greater than or equal to IQ1.
          
prob_am = st.norm.cdf(IQ1, 100,15) # write a command that calculates the probability that a randomly
          # selected person has is less than or equal to IQ1.
          
prob_bet = st.norm.cdf(IQ2,100,15) - st.norm.cdf(IQ1,100,15) 
            # write command that calculates the probability that a randomly
           # selected person has is between IQ1 and IQ2
            
print("The probability that a randomly selected person \n has an IQ of at least " + str(IQ1) + " is " + str(prob_al) + ".")
print("The probability that a randomly selected person \n has an IQ of at least " + str(IQ1) + " is " + str(prob_am) + ".")
print("The probability that a randomly selected person \n has an IQ of between " + str(IQ1) + " and " + str(IQ2)+ " is " + str(prob_bet) + ".")
