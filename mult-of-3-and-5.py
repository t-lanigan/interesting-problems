
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import time

n = 1000

#solution #1 (using brute force)
t0 = time.time()
s = 0
for i in range(1,n):
	if i % 3 == 0 or i % 5 == 0:
		s += i
print s
t1 = time.time()
print "Executed in:",t1 - t0


# solution #2 (using list comprehension)
print sum([x for x in range(1,n) if x % 3 == 0 or x % 5 == 0])
t2 = time.time()
print "Executed in:",t2 - t1

#solution #3 (using function definition) FASTEST!!
t3 = time.time()
def f(x): return x % 3 == 0 or x % 5 == 0
print sum(filter(f, range(1,n)))
print "Executed in:",t3 - t2

#solution #4(using lambda) So, real world good lambda use cases are very rare. 
# They are significantly slower as shown by the following:
t4 = time.time()
print sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1,n)))
print "Executed in:",t4 - t3