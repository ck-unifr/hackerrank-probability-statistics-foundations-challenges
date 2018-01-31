#https://www.hackerrank.com/challenges/basic-probability-puzzles-3/problem

X = ['r']*4 + ['b']*3
Y = ['r']*5 + ['b']*4
Z = ['r']*4 + ['b']*4

nb = 0

for b1 in X:
    for b2 in Y:
        for b3 in Z:
            if (b1=='b' and b2=='r' and b3=='r') or (b1 == 'r' and b2 == 'b' and b3 == 'r') or (b1 == 'r' and b2 == 'r' and b3 == 'b'):
                nb +=1

print('{}/{}'.format(str(nb), str(7*9*8)))


