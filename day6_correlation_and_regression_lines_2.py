# https://www.hackerrank.com/challenges/correlation-and-regression-lines-2/problem

# Task
# There are 2 series of data involving index numbers: P for price index and S for the commodity stock.
# The mean and standard deviation of P are 100 and 8, respectively.
# The mean and standard deviation of S are 103 and 4, respectively.
# The  R^2 correlation coefficient between the two series is 0.4.

# With this data, obtain the slope of the regression line of P on S, correct to a scale of 2 decimal places.

# Output Format
# Your answer should be a single floating point/decimal number, correct to a scale of 2 decimal places.


# https://www.hackerrank.com/challenges/correlation-and-regression-lines-2/forum

import math

# r = cov(x,y)/sd(x)/sd(y)
# r^2 = R^2
# slope = cov(x, y) / var(x)
# ->
# R^2 = slope^2 * var(x)^2 / sd(x)^2 / sd(y)^2

slope = math.sqrt(0.4 / (4**4/4**2/8**2))

print(round(slope, 2))