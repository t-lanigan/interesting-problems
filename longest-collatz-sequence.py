# Longest Collatz sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:

# n = n/2 (n is even)
# n = 3n + 1 (n is odd)

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.
def collatz_seq_len(n):
    seq = []
    while n != 1:
        seq.append(n)
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n+1
    seq.append(1)
    return len(seq)

l = []
max_len = 0
max_i = 0
for i in range(1,1000001):
    curr = collatz_seq_len(i)
    if curr >= max_len:
        max_len = curr
        max_i = i

print 'Number with longest collatz Sequence is:', max_i