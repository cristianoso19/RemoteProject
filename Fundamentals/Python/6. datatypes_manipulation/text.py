#single quotes combinable with double quotes
print('I am a "string"')
#output: I am a "string"

print("I am a 'string'")
#output: I am a 'string'


#multi line string with triple quotes
multilinestring = '''This is a multi line string
with triple quotes'''
print(multilinestring)
#output: This is a multi line string
#         with triple quotes

#length of a string
print(len(multilinestring))
#output: 46

#search for a substring in a string
print("string" in multilinestring)
#output: True

#search for not in a string
print("String" not in multilinestring)
#output: True
#observation: the search is case sensitive, so "String" would return False

#uppercase and lowercase
print(multilinestring.upper())
#output: THIS IS A MULTI LINE STRING
print(multilinestring.lower())
#output: this is a multi line string    

#space removal
stringwithspaces = "   Hello World   "
print(stringwithspaces.strip())
#output: Hello World

