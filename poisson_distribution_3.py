#https://www.hackerrank.com/challenges/poisson-distribution-3/problem
# The number of calls coming per minute into a hotels reservation center is Poisson random variable with mean 3.
#
# (a) Find the probability that no calls come in a given 1 minute period.
#
# (b) Assume that the number of calls arriving in two different minutes are independent.
# Find the probability that atleast two calls will arrive in a given two minute period.

import math,scipy.stats

print('%.3f'%scipy.stats.poisson.pmf(0,3))

#print('%.3f'%(1-2*scipy.stats.poisson.pmf(0,3)*scipy.stats.poisson.pmf(1,3)-scipy.stats.poisson.pmf(0,3)**2))
print('%.3f'%(1-scipy.stats.poisson.cdf(1, 3*2)))