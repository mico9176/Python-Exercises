'''
Computer Science Python Exercise 1

Instruction: Implement a program that requests a list of student names from the
user and prints those names that start with letters A through M.

Expected Output:

>> Enter a list: ['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin']
>> Ellie
>> Gavin

Notes on Constraints:
1. The input must be a list; it must have square brackets at the beginning and
at the end and the names that are in the list should be separated by commas and
must have an apostrophe at the beginning and at the end; they must also begin
with CAPITAL Letters.

2. If any these of these constraints are not followed, then an error will be
raised.
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
            if name[0] != "'" or name[-1] != "'":
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
    print("Error: One of the items in the list does not start/end with an apostrophe")
