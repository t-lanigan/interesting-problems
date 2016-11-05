import math
import time



# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

n = 2000000
# start = time.clock()

# # primality test
# def isprime(n):
#     if n == 2:
#         return True
#     if n % 2 == 0 or n <= 1:
#         return False

#     sqr = int(math.sqrt(n)) + 1

#     for divisor in range(3, sqr, 2):
#         if n % divisor == 0:
#             return False
#     return True


# def prime_sum(n):

#     return sum([x for x in range(1,n) if isprime(x)])


# print 'Finding sum of primes below %s' % n
# print (prime_sum(n))
# end = time.clock()
# print ("Running time : %s seconds" % (end - start))

# More efficient method using sieve of Eratosthanes
from array import array
start = time.clock()
def sieve(n):

    #initialize an array for a speed boost
    s = [False]*3 + [True, False]*(n/2-2)
    p = [2]

    for i,j in enumerate(s):
        if j:
            p.append(i)
            for k in range(i*i, (n-1), i):
                s[k] = False

    return sum(p)

print 'Finding sum of primes below {:,}.'.format(n)
print (sieve(n))
end = time.clock()
print ("Running time: {:.3f} seconds.".format(end - start))



