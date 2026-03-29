#strings
simplequote = 'I am a string'
doublequote = "I am also a string"
triplequote = '''I am a string too'''

print(simplequote)
print(doublequote)
print(triplequote)

#numbers
a = 5
b = 3.14
c = 2 + 3j

print(a)
print(b)
print(c)

#Lists: is a collection which is ordered and changeable. Allows duplicate members and has a index
list = [0, 1, 2, 3, 4, 5]

#tuples: is a collection which is ordered and unchangeable. Allows duplicate members and has a index
tuple = ("a", "b", "c", "d", "e")

#dictionaries: is a collection which is unordered, changeable and indexed. No duplicate members
dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

#sets: is a collection which is unordered and unindexed. No duplicate members
set = {1,1,2,2,3,3,4,4,5,5} 
#the set will only contain unique values, so it will be {1, 2, 3, 4, 5}

#boolean: is a data type that can only be True or False
is_true = True
is_false = False