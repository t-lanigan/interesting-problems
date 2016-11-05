

# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.What is the smallest positive number 
# that is evenly divisible by all of the numbers from 1 to 20?

#brute force.
# i = 20
# while ((i % 1 != 0) or (i % 2 != 0) or (i % 3 != 0) or (i % 4 != 0) or (i % 5 != 0) or 
# 	  (i % 6 != 0) or (i % 7 != 0) or (i % 8 != 0) or (i % 9 != 0) or (i % 10 != 0) or 
# 	  (i % 11 != 0) or (i % 12 != 0) or (i % 13 != 0) or (i % 14 != 0) or (i % 15!= 0) or 
# 	  (i % 16 != 0) or (i % 17 != 0) or (i % 18 != 0) or (i % 19 != 0) or (i % 20 != 0)):
# 	  i += 20

# print i

#better solution
# Find the smallest set of primes, such that all numbers 1-20 can be 
# constructed. This set will be the prime factorisation of the smallest 
# number to which 1-20 are all evenly divisible. So multiply them together.
import time
start = time.clock()
n = 40

def prime_factors(n):
	lst = []
	i = 2
	while i <= n:
		if n%i == 0:
			n = n/i
			lst.append(i)
		else:
			i += 1
	return lst
# returns a list of all the prime factors of number n
	
def count(lst): 
	keys = sorted(list(set(lst)))
	values = []
	for i in keys:
		values.append(lst.count(i))
	d = dict(zip(keys,values))
	return d
# returns a dictionary, where the keys are the elements of the list, 
# and the values are the number of occurrences of each element in the list

def lcm(n):
	lcm_dict = {}
	for i in range(n, 1, -1):
		for prime in count(prime_factors(i)):
			if prime not in lcm_dict or count(prime_factors(i))[prime] > lcm_dict[prime]:
				lcm_dict.update({prime: count(prime_factors(i))[prime]})
			else:
				pass
	print lcm_dict
# creates a consolidated dictionary of prime factors for all numbers in the range
	result = 1
	for prime in lcm_dict:
		result = result*(int(prime)**int(lcm_dict[prime]))
# counts Least Common Multiple
	return result
	
print (lcm(n))
		
end = time.clock()
print ("Running time : %s seconds" % (end - start))