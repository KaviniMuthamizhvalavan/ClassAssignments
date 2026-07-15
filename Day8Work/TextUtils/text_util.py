from collections import Counter
class TextUtils:
    def word_count(self, text):
        words = text.lower().split()
        count = Counter(words)
        return len(count.keys())
    
    def unique_words(self, text):
        words = text.lower().split()
        return list(set(words))
    
    def reverse_string(self, text):
        return text.lower()[::-1]

def main():
    obj = TextUtils()
    while True:
        print("\n===== Text Utilities =====")
        print("1. Word Count")
        print("2. Unique Words")
        print("3. Reverse String")
        print("4. Exit")

        ch = int(input("Enter your choice: "))
        if ch == 1:
            txt = input("Enter text: ")
            print("Word Count: ",obj.word_count(txt))
    
        elif ch == 2:
            txt = input("Enter text: ")
            print("Unique Words: ", obj.unique_words(txt))

        elif ch == 3:
            txt = input("Enter text: ")
            print("Reversed String: ", obj.reverse_string(txt))

        elif ch == 4:
            print("Exiting ...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()