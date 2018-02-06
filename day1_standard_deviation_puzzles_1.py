#https://www.hackerrank.com/challenges/standard-deviation-puzzles-1/problem

# Task
# Find the largest possible value of N where the standard deviation of the values in the set {1, 2, 3, N} is equal
# to the standard deviation of the values in the set {1, 2, 3}.

# Output the value of N, correct to two decimal places.

import math

def compute_sd(X):
    mean = sum(X) / len(X)
    X = [(x - mean) ** 2 for x in X]
    return math.sqrt(sum(X) / len(X))
    return sd


loop = True
N = 3
sd1 = compute_sd([1, 2, 3])
# print(sd1)
while loop:
    sd2 = compute_sd([1, 2, 3]+[N])
    # print(sd2)
    if round(sd1, 3) == round(sd2, 3):
        print(round(N, 2))
        loop = False
    N -= 0.01