# Let d(n) be defined as the sum of proper divisors of n 
# (numbers less than n which divide evenly into n).If d(a) = b 
# and d(b) = a, where a != b, then a and b are an amicable pair 
# and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11,
# 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors 
# of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import time
import math


def sum_of_div(x):
"Finds the sum of the divisors of the number"
    s = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if (x % i == 0):
            s += i
            s += x / i
    return s

def find_sum(n):
"find sum of amicable numbers below n"   
    sum = 0
    for i in range(1, n):
        x = sum_of_div(i)
        if (sum_of_div(x) == i):
            if (i != x):
                sum += i
    return sum


start = time.clock()
print find_sum(10000)
end = time.clock()

print 'Found in %s seconds' % (end - start)