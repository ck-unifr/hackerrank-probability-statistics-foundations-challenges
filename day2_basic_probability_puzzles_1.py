#https://www.hackerrank.com/challenges/basic-probability-puzzles-1/problem

# Task
# In a single toss of 2 fair (evenly-weighted) 6-sided dice,
# find the probability of that their sum will be at most 9.

sum_most_9 = 0
dice = [i+1 for i in range(6)]

for dice1 in dice:
    for dice2 in dice:
        sum = dice1 + dice2
        if sum <= 9:
            sum_most_9 += 1

print('{}/{}'.format(str(sum_most_9), '36'))
