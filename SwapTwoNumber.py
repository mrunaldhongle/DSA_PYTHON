# Write a program to swap two numbers using a temporary variable.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Before swapping: a=", a)
print("Before swapping: b=", b)
temp= a
a = b
b = temp
print("After swapping:a=", a)
print("After swapping:b=", b)