'''
Computer Science Python Exercise 4

Instruction: Implement a program that requests an integer n from the user
and prints on the screen the squares of all numbers from 0 up to, but not
including n

Expected Output:

>> Enter n: 4
>> 0
>> 1
>> 4
>> 9

Notes on Constraints:
1. The input must be an integer (i.e. ... ,-2,-1, 0, 1, 2, 3, ...); if the number
has only trailing zeroes on the end (e.g. 1.000, 1.0, 2.0, etc.), the program
will accept it.

2. If any these of these constraints are not followed, then an error will be
raised.
'''
try:
	n = float(input("Enter n: "))
	squareList = []

	if n % 1 == 0:
		if n > 0:
			for x in range(0, int(n)):
				print(x**2)
		else:
			for x in range(int(n+1), 1):
			    squareList.append(x**2)
			    squareList.sort()
			for square in squareList:
			    print(square)
	else:
		raise TypeError

except ValueError:
	print("Error: The value you entered is not a number")

except TypeError:
	print("Error: The number you entered is not an integer")
