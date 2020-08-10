'''
Computer Science Python Exercise 5

Instruction: Implement a program that requests a positive integer n and
prints on the screen all positive divisors of n

Expected Output:

>> Enter n: 49
>> 1
>> 7
>> 49

Notes on Constraints:
1. The input must be a positive integer (i.e. 1, 2, 3, 4, 5, ...); if the number
has only trailing zeroes on the end (e.g. 1.000, 1.0, 2.0, etc.), the program
will accept it.

2. If any these of these constraints are not followed, then an error will be
raised.
'''
try:
	n = float(input("Enter n: "))

	if n > 0 and n % 1 == 0:
		for x in range(1, int(n)+1):
			if n % x != 0:
				continue
			print(x)
	else:
		raise TypeError

except ValueError:
	print("Error: The value you entered is not a number")

except TypeError:
	print("Error: The number you entered is not a positive integer")
