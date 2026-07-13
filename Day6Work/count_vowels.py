#func to count vowels

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

def count_vowels2(s):
    vowels = "aeiou"
    count = 0
    while s:
        char = s[0].lower()
        if char in vowels:
            count += 1
        s = s[1:]
    return count

#user input
user_input = input("Enter a string to count vowels: ")
result = count_vowels(user_input)
print(f"The number of vowels in '{user_input}' is: {result}")

user_input2 = input("Enter another string to count vowels using the second method: ")
result2 = count_vowels2(user_input2)
print(f"The number of vowels in '{user_input2}' is: {result2}")