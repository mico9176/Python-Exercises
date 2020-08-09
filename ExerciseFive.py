'''
Computer Science Python Exercise 5

Instruction: Implement a program that requests an integer n and
prints on the screen all positive divisors of n

Expected Output:

>> Enter n: 49
>> 1
>> 7
>> 49
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
