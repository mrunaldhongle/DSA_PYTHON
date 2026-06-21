#Write a program to convert an octal number to its decimal representation.
def octal_to_decimal(octal):
    decimal = 0
    base = 1
    while octal > 0:
        last_digit = octal % 10
        decimal += last_digit * base
        base *= 8
        octal //=10
    return decimal
octal_value = int(input("Enter an octal number: "))
decimal_value = octal_to_decimal(octal_value)
print(f"The decimal equivalent of octal number {octal_value} is: {decimal_value}")