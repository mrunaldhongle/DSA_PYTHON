#Check if a Number is Palindrome
def is_palindrome(num):
    original = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //=10
    return original == reversed_num
n = int(input("Enter a number to check if it is a palindrome: "))
if is_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")