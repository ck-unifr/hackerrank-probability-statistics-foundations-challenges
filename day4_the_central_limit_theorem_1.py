#https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

# Task
# A large elevator can transport a maximum of 9800 pounds.
# Suppose a load of cargo containing 49 boxes must be transported via the elevator.
# The box weight of this type of cargo follows a distribution with a mean of 205 pounds
# and a standard deviation of 15 pounds.
# Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator
# and transported?

import math

def clf(x, mean, sd):
  return 0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5))))

max = 9800
n = 49
mean_pop = 205
sd_pop = 15

mean_sample = mean_pop * n
sd_sample = math.sqrt(n) * sd_pop

print(round(clf(max, mean_sample, sd_sample), 4))