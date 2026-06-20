#Write a program to convert a decimal number to its hexadecimal representation.
def convert_to_hexadecimal(num):
    if num == 0:
        return "0"
    hexadecimal = []
    while num > 0:
        rem = num % 16
        if rem < 10:
            hexadecimal.append(str(rem))
        else:
            hexadecimal.append(chr(rem - 10 + ord('A')))
        num = num // 16
    hexadecimal.reverse()
    return ''.join(hexadecimal)
n = int(input("Enter the decimal Number: "))
hexadecimal_representation = convert_to_hexadecimal(n)
print(f"Hexadecimal representation of {n} is: {hexadecimal_representation}")