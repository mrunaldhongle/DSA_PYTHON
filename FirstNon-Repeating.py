# to find the first unique character that doesn't repeat, indicating a rare event.
def first_non_repeating(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in s:
        if count[char] == 1:
            return char
    return None
s = input("Enter a string: ")
result = first_non_repeating(s)
if result:
    print("The first non-repeating character is:", result)
else:
    print("No non-repeating character found.")
    