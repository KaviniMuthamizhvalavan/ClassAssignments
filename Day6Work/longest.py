'''
write a python program to find the longest word in a sentence. 
requirements:
1. create a function names find_longest_word()
2. accept a sentence as input from the user
3. split the sentence into words
4. find the longest word in the list of words
5. return the longest word
6. display the result to the user
'''

def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return longest_word

def find_longest_word2(sentence):
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

sentence = input("Enter a sentence: ")
longest_word = find_longest_word(sentence)
print(f"The longest word in the sentence is: '{longest_word}'")

sentence2 = input("Enter another sentence: ")
longest_word2 = find_longest_word2(sentence2)
print(f"The longest word in the second sentence is: '{longest_word2}'")