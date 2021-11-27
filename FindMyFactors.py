# This functions finds the factors of an integer.

def factors(b):

	for i in range(1, b+1):  # This iterates from 1 to b
		if b % i == 0:
			print(i)

if True:

	b = input('Your Number Please: ')
	b = float(b)

	if b > 0 and b.is_integer():
		factors(int(b))
	else:
		print('Please enter a positive integer')

