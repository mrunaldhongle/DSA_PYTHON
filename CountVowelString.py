#Count Vowels in a String
s = input().lower()
vowels = 'aeiou'
count = sum(1 for char in s if char in vowels)
print("Number of vowels in the string:", count)