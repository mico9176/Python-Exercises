'''
Computer Science Python Exercise 3

Instruction: Implement a program that request a positive integer n from the user
and prints the first four multiples of n.

Expected Output:

>> Enter n: 5
>> 0
>> 5
>> 10
>> 15
'''

try:
	n = float(input("Enter n: "))

	if n > 0 and n % 1 == 0:
		for x in range(0, 4):
			print(int(n)*x)
	else:
		raise TypeError

except ValueError:
	print("Error: The value you entered is not a number")

except TypeError:
	print("Error: The number you entered is not a positive integer")
