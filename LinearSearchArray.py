#Linear Search in Array
n = int(input("Enter the number of elements in an array: "))
arr = list(map(int, input().split()))
key = int(input())
index = -1
for i in range(n):
    if arr[i] == key:
        index = i
        break
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")