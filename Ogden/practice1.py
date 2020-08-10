'''
Computer Science Python Practice 1:

Instruction: Implement a program that requests a list of words from the user
and then prints each word in the list that is not 'secret'.

Expected output:

>> Enter list of words: ['cia','secret','mi6','isi','secret']
>> cia
>> mi6
>> isi

Notes on Constraints:
1. The input must be a list; it must have square brackets at the beginning and
at the end and the words that are in the list should be separated by commas and
must have an apostrophe at the beginning and at the end.

2. If any these of these constraints are not followed, then an error will be
raised.
'''
try:
    list_input = input("Enter list of words: ")
    list = []

    if list_input[0] == '[' and list_input[-1] == ']':
        list_input = list_input.replace('[', '')
        list_input = list_input.replace(']', '')
        list_input = list_input.replace(' ', '')
        list = list_input.split(',')

        for word in list:
            if word[0] != "'" or word[-1] != "'":
                raise SyntaxError

        for word in list:
            word = word.replace("'", '')
            if word != "secret":
                print(word)

    else:
        raise ValueError

except ValueError:
	print("Error: The value you entered is not a list")

except SyntaxError:
    print("Error: One of the items in the list does not start/end with an apostrophe")
