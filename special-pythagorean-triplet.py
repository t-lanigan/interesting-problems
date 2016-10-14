

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import math
import time

def boundary_cond(a,b):
	return (a + b + math.sqrt(a**2+b**2) == 1000)

def calc_prod(a,b):
	return int(math.sqrt(i**2 + j**2) * i * j)

start = time.clock()

product = 0
for i in range(1000):
	for j in range (i+1,1000):
		if i == 0 or j == 0:
			continue
		elif boundary_cond(i,j):
			product = calc_prod(i,j)
			break
	if product != 0:
		break	


end = time.clock()

print 'Product =', product
print 'a =', i
print 'b =', j
print 'c =', int(math.sqrt(i**2+j**2))
print 'Running time is:', (end-start)
