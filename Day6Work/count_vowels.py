#func to count vowels

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

#user input
user_input = input("Enter a string to count vowels: ")
result = count_vowels(user_input)
print(f"The number of vowels in '{user_input}' is: {result}")