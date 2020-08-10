# practice
y = input('Enter a list of words: ').strip()
r = ["[","'","’","]",]
for c in r:
    y = y.replace(c, "")
y = y.split(",")
for ap in y:
    if ap != "secret":
        print(ap)
# number 1
y = input('Enter list: ').strip()
r = ["[","'","’","]"]
for c in r:
    y = y.replace(c, "")
y = y.split(",")
letters = 'ABCDEFGHIJKLM'
for ap in y:
    ap.strip()
    if (letters.find(ap[0]) != -1):
        print(ap)
# number 2        
y = input('Enter a list: ').strip()
y = y[1:-1]
y = y.split(",")
print('The first list element is '+y[0].strip())
print('The last list element is '+y[-1].strip())
# number 3
n = int(input('Enter n: '))
for x in range(4): 
    print(x*n)
# number 4
n = int(input('Enter n: '))
for x in range(n):
    print(x ** 2)
# number 5
n = int(input('Enter n: '))
for x in range(n):
    if (n % (x+1)) == 0:
        print(x+1)
# number 6
a = 0
for n in range(4):
    if n != 3:
        if n == 0:
            s = 'first'
        elif n == 1:
            s = 'second'
        else:
            s = 'third'
        a = a + float(input('Enter '+s+' number: '))
    else:
        if (a / 3) == float(input('Enter last number: ')):
            print('Equal')