a = input("Geef getal tussen 2 en 91: ")
p = 91
k = 29
b = pow(int(a), 5)
c = b%p
print('Eerste modulo een is: ' + str(c))
d = pow(c, k)
print(str(c) + ' power 29: ' + str(d))
b = d%p
print('De uitkomst via het Magic Number is: ' + str(b))

if int(a) == b:
    print('Proof of concept')
else:
    print('Proof of concept is false')
