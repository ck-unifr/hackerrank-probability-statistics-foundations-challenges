#https://www.hackerrank.com/challenges/standard-deviation-puzzles-3/problem

# Let X and Y be two independent "normal" random deviates with mean and standard deviation 10 and 3,
# and 20 and 4, respectively. Let sigma be the value of the standard deviation of the distribution
# obtained by adding the two distributions ( X + Y ).

# In the answer box, enter the value of sigma, correct to one place of decimal.

import math

mu1 = 10
mu2 = 20
sd1 = 3
sd2 = 4

print('%.1f' % math.sqrt(sd1**2 + sd2**2))