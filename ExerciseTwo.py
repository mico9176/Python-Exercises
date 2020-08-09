'''
Computer Science Python Exercise 2

Instruction: Implement a program that requests a non-empty list from the user
and prints on the screen a message giving the first and last element of the list.

Expected Output:

>> Enter a list:  [3, 5, 7, 9]
>> The first list element is 3
>> The last list element is 9
'''
try:
    list_input = input("Enter a list: ")
    list = []

    if list_input[0] == '[' and list_input[-1] == ']':
        list_input = list_input.replace('[', '')
        list_input = list_input.replace(']', '')
        list = list_input.split(',')

        print("The first list element is " + list[0])
        print("The last list element is" + list[-1])
    else:
        raise ValueError

except ValueError:
	print("Error: The value you entered is not a list")
