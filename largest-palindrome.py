

# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# def check_if_palindrome(n):
# 	digits = map(int, str(n))
# 	return digits == digits[::-1] 

# max_fact1 = 0
# max_fact2 = 0
# pal = 0
# for i in range(1,999):
# 	for j in range(1,999):
# 		prod = i * j
# 		if check_if_palindrome(prod) and prod > pal:
# 			max_fact1 = i
# 			max_fact2 = j
# 			pal = prod

# print 'Largest palindrome:', pal

# Better Solution:

max_pal = max([i*j for i in range(100,1000) for j in range(100,1000) if str(i*j) == str(i*j)[::-1]])

print 'Largest palindrome:', max_pal


