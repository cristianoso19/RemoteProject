#To work with strings we have to know how to slice them. Slicing is a way to extract a portion of a string by specifying the start and end indices.

text = "this is a text"

print(text[0:15]) 
#Output: this is a text
#in the end index is not included, so it will print from index 0 to index 14

print(text[:8])
#Output: this is
#If the start index is not specified, it defaults to 0, so it will print from index 0 to index 7

print(text[4:8])
#Output: is a

print(text[:-2])
#Output: this is a tex
#If the end index is negative, it counts from the end of the string, so it will print from index 0 to index -3 (which is the last character 't' in this case)

course = "Python for Beginners"
print(course.replace("Beginners", "Dumbs"))
#Output: Python for Dumbs
#The replace() method is used to replace a specified substring with another substring. In this case, it replaces "Beginners" with "Dumbs".

#split
split_text = course.split(" ")
print(split_text)
#Output: ['Python', 'for', 'Beginners']
#The split() method is used to split a string into a list of substrings based on a specified delimiter. In this case, it splits the string at each space character, resulting in a list of words.

#normalize the text
print("python".lower() in course.lower())
#Output: True
#The lower() method is used to convert all characters in a string to lowercase. In this case, it converts both "python" and "course" to lowercase before checking if "python" is in "course". Since "python" is indeed in "course" (after converting both to lowercase), it returns True.

