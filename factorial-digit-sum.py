
# The sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import math
n = 100

print sum([int(d) for d in str(math.factorial(n))])