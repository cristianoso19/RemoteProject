import random

x = 1
y = 2.5
z = 1j

print(type(x))
print(type(y))
print(type(z))
#output: <class 'int'>
#        <class 'float'>
#        <class 'complex'>

positive = 1
negative = -1

imaginary = -5 - 1j
#output: -5 - 1j

#casting
xf = float(x)
print(type(xf))
#output: <class 'float'>
print(xf)
#output: 1.0

yi = int(y)
print(type(yi))
#output: <class 'int'>
print(yi)
#output: 2 be careful when casting from float to int, it will truncate the decimal part and not round it

#complex casting
xj = complex(x)
print(xj)
print(type(xj))
#output: (1+0j) 
#output: <class 'complex'>

yj = complex(y)
print(yj)
print(type(yj))
#output: (2.5+0j)
#output: <class 'complex'>

#random number generation
print(random.randint(1, 10))#number between 1 and 9 




