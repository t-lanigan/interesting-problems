import math
import time
n = 10000

# Square sum - sum square
print '\nBrute force method for n = %s' %n
start = time.clock()
print sum([x for x in xrange(1,n+1)])**2-sum([x**2 for x in xrange(1,n+1)])
end = time.clock()
print ("Running time : %s seconds" % (end - start))


print '\nMathematical method for n = %s' %n
start = time.clock()

a = (n*(n+1)/2)**2
b = n*(n+1)*(2*n+1)/6
print a-b

		
end = time.clock()
print ("Running time : %s seconds\n" % (end - start))