# check if a candidate number is prime to ensure secure prime factors for encryption algorithms.
import math 
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True
n = int(input("Enter a number to check if it is prime:"))
if is_prime(n):
    print("yes")
else:
    print("no")
