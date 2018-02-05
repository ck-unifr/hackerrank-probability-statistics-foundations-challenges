#https://www.hackerrank.com/challenges/the-central-limit-theorem-2/problem

# Task
# The number of tickets purchased by each student for the University X vs. University Y football game
# follows a distribution that has a mean of 2.4 and a standard deviation of 2.0.
#
# A few hours before the game starts, 100 eager students line up to purchase last-minute tickets.
# If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?


import math

def clf(x, mean, sd):
  return 0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5))))


nb_tickets = 250
nb_students = 100
mean = 2.4
std = 2.0

mean_sample = mean * nb_students
sd_sample = std * math.sqrt(nb_students)

print(round(clf(nb_tickets, mean_sample, sd_sample), 4))
