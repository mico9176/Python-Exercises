'''
Computer Science Python Exercise 6

Instruction: Implement a program that requests an four numbers (integer or
floating-point) from the user. Your program should compute the average of the
first three numbers and compare the average to the fourth number. If they are
equal, your program should print 'Equal' on the screen

Expected Output:

>> Enter first number: 4.5
>> Enter second number: 3
>> Enter third number: 3
>> Enter last number: 3.5
>> Equal
'''
try:
    w = float(input("Enter first number: "))
    x = float(input("Enter second number: "))
    y = float(input("Enter third number: "))
    z = float(input("Enter last number: "))

    if (w+x+y)/3 == z:
    	print("Equal")
    else:
    	print("Not equal")

except ValueError:
    print("Error: The value you enetered is not an integer nor a floating-point")
