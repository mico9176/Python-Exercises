'''
Computer Science Python Exercise 1

Instruction: Implement a program that requests a list of student names from the
user and prints those names that start with letters A through M.

Expected Output:

>> Enter a list: ['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin']
>> Ellie
>> Gavin
'''
try:
    list_input = input("Enter a list: ")
    list = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

    if list_input[0] == '[' and list_input[-1] == ']':
        list_input = list_input.replace('[', '')
        list_input = list_input.replace(']', '')
        list_input = list_input.replace(' ', '')
        list = list_input.split(',')

        for name in list:
            if name[0] != "'" and name[-1] != "'":
                raise SyntaxError

        for name in list:
            name = name.replace("'", '')
            for letter in letters:
                if name.startswith(letter):
                    print(name)
    else:
        raise ValueError

except ValueError:
	print("Error: The value you entered is not a list")

except SyntaxError:
    print("One of the items in the list does not start with an apostrophe")
