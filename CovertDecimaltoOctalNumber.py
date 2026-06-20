#write a program to convert a decimal number to its actal representation
def convert_to_octal(num):
    if num== 0:
        return "0"
    octal =[]
    while num > 0:
        octal.append(str(num % 8))
        num = num // 8
    octal.reverse()
    return ''.join(octal)
n = int(input("Enter a decimal number: "))
octal_representation = convert_to_octal(n)
print(f"Octal representation of {n} is : {octal_representation}")