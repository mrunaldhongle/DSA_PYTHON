# Write a program to convert a decimal number to its binary equivalent.
def convert_to_binary(num):
    if num == 0:
        return "0"
    binary = []
    while num > 0:
        binary.append(str(num%2))
        num = num // 2
    binary.reverse()
    return ''.join(binary)
n = int(input("Enter a decimal number: "))
binary_representation = convert_to_binary(n)
print(f"binary representation of {n} is: {binary_representation}")