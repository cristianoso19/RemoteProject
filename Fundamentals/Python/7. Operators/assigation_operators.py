#Assignment Operators
x = 10
print(x) #Output: 10

x += 5
print(x) #Output: 15 (x = x + 5)
x -= 3
print(x) #Output: 12 (x = x - 3)
x *= 2
print(x) #Output: 24 (x = x * 2)
x /= 4
print(x) #Output: 6.0 (x = x / 4) float division
x %= 4
print(x) #Output: 2.0 (x = x % 4) remainder

y = 20

y //= 3
print(y) #Output: 6 (y = y // 3) floor division, discards the decimal part
y **= 2
print(y) #Output: 36 (y = y ** 2) y raised to the power of 2

#Walrus operator (Python 3.8+)
#The walrus operator (:=) allows you to assign a value to a variable as part of an expression. It is useful for situations where you want to use the value of a variable immediately after assigning it, without needing to write a separate assignment statement.
if (n := len("Hello")) > 5:
    print(f"The length of the string is greater than 5: {n}")
    #Output: The length of the string is not greater than 5: 5
else:
    print(f"The length of the string is not greater than 5: {n}") #Output: The length of the string is not greater than 5: 5