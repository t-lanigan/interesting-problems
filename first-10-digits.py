# Large sum
# Problem 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

#hard to read code, but funny. Opens the file, splits by line into list, maps to int, sums, maps to str, prints first 10 chrs.
print str(sum(map(int, open('100-50-digit-nums.txt').read().splitlines())))[0:10]