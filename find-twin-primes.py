# find twin prime between 1 thousand to 1 million
def isPrime(n):
    if n == 2 or n == 3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    return True
def isTwinPrime(n):
    if isPrime(n) and isPrime(n+2): return True
j=0
import numpy as np
x=np.zeros(1000000)
for i in range(1000,1000000):
    if isTwinPrime(i):
        x[j]=i
        j=j+1
print('number of twim primes=',j,'maxmimum twim primes=', x[j-1], x[j-1]+2,sep='\n' )
