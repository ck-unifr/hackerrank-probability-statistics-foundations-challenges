#https://www.hackerrank.com/challenges/standard-deviation-puzzles-2/problem

# Task
# The heights of a group of children are measured.
# The resulting data has a mean of 0.675 meters, and a standard deviation of 0.065 meters.
# One particular child is 90.25 centimeters tall.
# Compute z, the number of standard deviations away from the mean that the particular child is.

# Enter the value of z, correct to a scale of two decimal places.

mu = 0.675
sd = 0.065
x = 0.9025

z = (x - mu)/sd

print('%.2f' % (z))