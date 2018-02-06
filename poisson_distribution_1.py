#https://www.hackerrank.com/challenges/poisson-distribution-1/problem

 # A random variable X follows Poisson distribution with mean 2.5,
# find the probability with which the random variable X is equal to 5; i.e. P(X = 5).


from scipy.stats import poisson

x = 5
mu = 2.5

prob = poisson.pmf(x, mu)

print(round(prob, 4))