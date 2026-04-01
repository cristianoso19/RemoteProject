#While is a loop that continues to execute as long as a certain condition is true. For example, if we want to print the numbers from 1 to 10, we can use a while loop like this:

i = 1
while i <= 10:
    print(i) #Output: 1 3 5 7 9
    if i == 5:
        break #This will exit the loop when i is equal to 5
    i += 2 #This is equivalent to i = i + 2
else:
    print("Loop ended") #This will not be executed because the loop is exited with break statement.

#For loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.
#Use continue to skip the current iteration and move to the next one.
