#for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects. For example, if we want to print the numbers from 1 to 10, we can use a for loop like this:
for letter in "Python":
    print(letter) #Output: P y t h o n

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) #Output: apple banana cherry

#Use continue to skip the current iteration and move to the next one.
for number in range(1, 11):
    if number % 2 == 0:
        continue #This will skip the even numbers and only print the odd numbers
    print(number) #Output: 1 3 5 7 9 

#Use break to exit the loop when a certain condition is met.
for number in range(1, 11):
    if number == 5:
        break #This will exit the loop when number is equal to 5
    print(number) #Output: 1 2 3 4

#use else with for loop, the else block will be executed when the loop is exhausted (when there are no more items to iterate over) and not when the loop is exited with a break statement.
for number in range(1, 6):
    print(number) #Output: 1 2 3 4 5
else:
    print("Loop ended") #Output: Loop ended 
#range() function is used to generate a sequence of numbers. It takes three arguments: start, stop, and step. The start argument is the number to start from (default is 0), the stop argument is the number to stop at (not included in the sequence), and the step argument is the increment between each number in the sequence (default is 1). For example, if we want to generate a sequence of numbers from 0 to 9, we can use the range() function like this:
for number in range(10):
    print(number) #Output: 0 1 2 3 4 5 6 7 8 9

for i in range(1, 11, 2):
    print(i) #Output: 1 3 5 7 9 (start from 1, stop at 10, and increment by 2)

#Nested for loops are used to iterate over a sequence of sequences. For example, if we want to print a multiplication table, we can use nested for loops like this:

fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit in fruits:
    for color in colors:
        print(f"{color} {fruit}") 
    '''#Output: red apple, 
    yellow apple, 
    green apple, 
    red banana, 
    yellow banana, 
    green banana, 
    red cherry, 
    yellow cherry, 
    green cherry'''