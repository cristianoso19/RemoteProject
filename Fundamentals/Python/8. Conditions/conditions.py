
x = 5
y = 3
z = 2

if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("No condition is complete")

if x > y and x > z:
    print("x is greater than y and z")
elif x == y:
    print("x is equal to y")
else:
    print("No condition is complete")
    
a = "Python"
b = "Java"
c = "C#"

if a == c:
    if a != b:
        print("a is equal to c but not equal to b")
    else:
        print("a is equal to c and b in intern if")
else:
    print("a is not equal to c")

e = 10
f = 10

if e == f:
    pass # This is a placeholder for future code, it does nothing and allows the program to run without errors.