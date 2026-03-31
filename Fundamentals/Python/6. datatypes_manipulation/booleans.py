#booleans can be either True or False
v = True
f = False
print(v) #Output: True
print(f) #Output: False

print(5>3) #Output: True
print(5<3) #Output: False

print(type(v)) #Output: <class 'bool'>

print(bool("Hello")) #Output: True
print(bool("")) #Output: False

#True
print(bool("abc")) #Output: True
print(bool(123)) #Output: True
print(bool([1, 2, 3])) #Output: True

#False
print(bool("")) #Output: False
print(bool(0)) #Output: False
print(bool([])) #Output: False
print(bool(None)) #Output: False

#isinstance() function is used to check if an object is an instance of a specific class or type. It returns True if the object is an instance of the specified class or type, and False otherwise.
x = 123
print(isinstance(x, int)) #Output: True
print(isinstance(x, str)) #Output: False
print(isinstance(x, float)) #Output: False