def listInput():
    main = input('Enter a list of words:').split()
    out = []
    for term in main:
        term = term.replace('[', '')
        term = term.replace(']', '')
        term = term.replace(',', '')
        term = term.replace("'", '')
        out += [term]
    return out

myInput = listInput()
for term in myInput:
    if term != 'secret':
        print(term)
