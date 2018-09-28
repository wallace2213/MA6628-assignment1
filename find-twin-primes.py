# find twin prime between 1 thousand to 1 million
# figure out whether a integer is a prime number
def isPrime(n):
    if n == 2 or n == 3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
# figure out whether twin integers are twin primes
def isTwinPrime(n):
    if isPrime(n) and isPrime(n+2): return True
# find out the total number and the maxmimum twim primes between 1k and 1m
j=0
import numpy as np
x=np.zeros(1000000)
for i in range(1000,1000000):
    if isTwinPrime(i):
        x[j]=i
        j=j+1
print('number of twim primes=',j,'maxmimum twim primes=', x[j-1], x[j-1]+2,sep='\n' )

# result and output
# number of twim primes=
# 8134
# maxmimum twim primes=
# 999959.0
# 999961.0
