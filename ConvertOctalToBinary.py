#write a program to convert octal number to Binary number
def octal_to_decimal(octal):
    decimal = 0
    base = 1 
    while octal > 0:
        last_digit = octal % 10
        decimal += last_digit * base
        base *= 8
        octal //= 10
    return decimal
    
def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = []
    while decimal > 0:
        binary.append(str(decimal % 2 ))
        decimal //=2
    binary.reverse()
    return ''.join(binary)

octal_value = int(input("Enter an octal number: "))
decimal_value = octal_to_decimal(octal_value)
binary_value = decimal_to_binary(decimal_value)
print(f"The binary equivalent of octal number {octal_value} is: {binary_value}")
