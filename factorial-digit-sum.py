
# The sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!


n = 100
total = 1

for i in xrange(n,0,-1):
    total *= i
    
print sum(map(int, str(total)))