#https://www.hackerrank.com/challenges/basic-probability-puzzles-2/problem

# Task
# For a single toss of 2 fair (evenly-weighted) dice,
# find the probability that the values rolled by each die will be different and their sum is 6.

sum_different_6 = 0
dice = [i+1 for i in range(6)]

for dice1 in dice:
    for dice2 in dice:
        sum = dice1 + dice2
        if sum == 6 and dice1 != dice2:
            sum_different_6 += 1

print('{}/{}'.format(str(sum_different_6), '36'))
