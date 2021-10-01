'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

def factors(number):
    for i in range(1, number + 1):
        if (number % i == 0):
            yield i;

def primes(arr):
    for i in arr:
        facs = list(factors(i));
        if len(facs) == 2:
            yield i;

number = 12;

factors = list(factors(number));

primeFactors = list(primes(factors));

print(primeFactors);