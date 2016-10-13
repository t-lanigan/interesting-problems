import math
import time

"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""
n = 10001
start = time.clock()

# primality test
def isprime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

        
def generateprime():
    num = 2
    while True:
        if isprime(num):
            #yield stops the loop and surrenders the number nth prime below
            yield num
            num += 1
        else:
            num += 1
            continue
            
def nthprime(nth):
    x = generateprime()
    result = []
    for num in range (1, nth + 1):
        result.append(next(x))
    return result

print 'Finding %s primes' % n
print (nthprime(n))
end = time.clock()
print ("Running time : %s seconds" % (end - start))