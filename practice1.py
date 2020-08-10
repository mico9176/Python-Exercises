'''
Computer Science Pyton Exercise 1:

Instruction: Implement a program that requests a list of words from the user
and then prints each word in the list that is not 'secret’.

Expected output:

>> Enter list of words: ['cia','secret','mi6','isi','secret’]
>> cia
>> mi6
>> isi
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
    print("One of the items in the list does not start/end with an apostrophe")
