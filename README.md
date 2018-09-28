# MA6628-assignment1
# this project is to find out the total number of twin primes between 1 thousand and 1 million
# the biggest twin prime is also an output of this project
# A twin prime is a prime number that is either 2 less or 2 more than another prime number, see for details here: https://en.wikipedia.org/wiki/Twin_prime

# code and description
def isPrime(n):   # figure out whether a integer is a prime number
    if n == 2 or n == 3: return True   # 2 and 3 are prime numbers
    if n%2==0 or n<2: return False   # even numbers are not prime numbers
    for i in range(3,int(n**0.5)+1,2): # as even numbers are not prime numbers, here only consider odd numbers
        if n%i==0:
            return False         # if a number can be divided by another number in the range of 3 to root n, it is not a prime number
    return True

# figure out whether twin integers are twin primes
def isTwinPrime(n):
    if isPrime(n) and isPrime(n+2): return True  # if n and n+2 are both prime numbers, they are twin prime

# find out the total number and the maxmimum twim primes between 1k and 1m
j=0
import numpy as np
x=np.zeros(1000000)
for i in range(1000,1000000):
    if isTwinPrime(i):
        x[j]=i                  # x[j] stores the smaller one of the twin prime
        j=j+1                   # j is the total number of twin prime
print('number of twim primes=',j,'maxmimum twim primes=', x[j-1], x[j-1]+2,sep='\n' )



# result and output
# number of twim primes=
# 8134
# maxmimum twim primes=
# 999959.0
# 999961.0
