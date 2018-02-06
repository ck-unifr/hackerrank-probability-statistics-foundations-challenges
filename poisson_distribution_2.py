#https://www.hackerrank.com/challenges/poisson-distribution-2/problem

# The manager of a industrial plant is planning to buy a machine of either type A or type B.
# For each day’s operation the number of repairs X, that the machine A needs is a poisson random variable with mean 0.88.
# The daily cost of operating A is
# C_A = 160 + 40+ X^2

# For machine B, let Y be the poisson random variable indicating the number of daily repairs,
# which has mean 1.55, and the daily cost of operating B is
# C_B = 128 + 40 + Y^2


lam_A = 0.88
lam_B = 1.55


C_A = 160 + 40*(lam_A + lam_A**2)
C_B = 128 + 40*(lam_B + lam_B**2)

print(round(C_A, 3))
print(round(C_B, 3))