import sys
from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker()
    while True:
        print("\n--- MENU ---")
        print("1. Enter a word")
        print("2. Exit")

        choice = input("select an option: ")

        if choice == "1":
            word = input("Enter a word: ").strip()
        elif choice == "2":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option!")
def display_results(word, anagrams):
    print("\n" + "=" * 40)
    print(f'YOUR WORD: "{word}"')
    print("This is a valid English word")

    if anagrams:
        formatted_anagrams = ", ".join(anagrams)
        print(f"Anagrams for your word: {formatted_anagrams}")
    else:
        print(f"No anagrams for your word")

if __name__ == "__main__":
    main()
