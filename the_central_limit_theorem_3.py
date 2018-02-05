#https://www.hackerrank.com/challenges/the-central-limit-theorem-3/problem

# You have a sample of 100 values from a population with mean µ = 500 and with standard deviation σ = 80.
# What is the probability that the sample mean will be in the interval (490, 510)?

import math

def clf(x, mean, sd):
  return 0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5))))

mean = 500
sd = 80
sample_size = 100

mean_sample = mean * sample_size
sd_sample = math.sqrt(sample_size) * sd

p1 = clf(510*sample_size, mean_sample, sd_sample)
p2 = clf(490*sample_size, mean_sample, sd_sample)


print(round(p1 - p2, 4))