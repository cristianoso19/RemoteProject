#Comparation operators are used to compare two values and return a boolean result (True or False)
x = 10
y = 5
z = 3

print(x == y) #Output: False (x is not equal to y)
print(x != y) #Output: True (x is not equal to y)
print(x > y) #Output: True (x is greater than y)
print(x < y) #Output: False (x is not less than y)
print(x >= z) #Output: True (x is greater than or equal to z)
print(y <= z) #Output: False (y is not less than or equal to z) 

#multiple comparisons
print(x > y > z) #Output: True (x is greater than y and y is greater than z)
print(x > y < z) #Output: False (x is greater than y but y is not less than z)

print(x>y and y>z) #Output: True (x is greater than y and y is greater than z)
print(x>y or y<z) #Output: True (x is greater than y or y is less than z)

v = True
f= False
print(not v) #Output: False (not operator negates the boolean value of v)
print(not f) #Output: True (not operator negates the boolean value of f)