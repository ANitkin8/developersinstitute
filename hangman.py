import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
             'credit card', 'rush', 'south']
word = random.choice(wordslist)
spaces = len(word)
guessed_letters = set()
lives = 6

Gallows_Stages = [
#starting point
""" 
   +---+
   |   |
       |
       |
       |
       |
   =========""",
#Index 1: 1 wrong guess(Head)
"""
   +---+
   |   |
   O   |
       |
       |
       |
 =========""",

    # Index 2: 2 wrong guesses (Torso)
"""
   +---+
   |   |
   O   |
   |   |
       |
       |
  =========""",

    # Index 3: 3 wrong guesses (Left Arm)
"""
   +---+
   |   |
   O   |
  /|   |
       |
       |
  =========""",

    # Index 4: 4 wrong guesses (Right Arm)
"""
   +---+
   |   |
   O   |
  /|\\ |
       |
       |
  =========""",

    # Index 5: 5 wrong guesses (Left Leg)
"""
   +---+
   |   |
   O   |
  /|\\ |
  /    |
       |
   =========""",

    # Index 6: 6 wrong guesses (Full Body)
"""
   +---+
   |   |
   O   |
  /|\\ |
  / \\ |
       |
   ========="""

]
while True:
    display = [char if char in guessed_letters or not char.isalpha() else '_' for char in word]
    print(Gallows_Stages[6 - lives])
    print("".join(display))

    if "_" not in display:
        print("congratulations! you guessed the word!")
        break
    if lives == 0:
        print("\nGame Over!")
        print(f"The word was '{word}'")
        break

    letter = input("\nPlease enter a letter (A-Z).").strip().lower()

    if len(letter) != 1 or not letter.isalpha():
        print("invalid input. Please enter a single letter (A-Z).")
        continue

    if letter in guessed_letters:
        print("already guessed. try a different letter.")
        continue
    guessed_letters.add(letter)
    if letter in word:
        print(f"Yes! '{letter}' is in the word.")
    else:
        print("sorry, your letter is not in the word")
        lives -= 1


