#Write a program to swap two numbers without using a temporary variable.
a = int(input("Enter the First Number: "))
b = int(input("Enter the Second Number: "))
print("Before swapping:a=", a)
print("Before swapping:b=",b)
a = a + b
b = a - b
a = a - b
print("After swapping:a=", a)
print("After swapping:b=", b)