import random
def number_guessing_game():
    random_number = random.randint(1, 100)
    max_attemps = 7
    for attempt in range(max_attemps):
        guess = int(input("guess a number between 1 and 100\n"))

        if guess > random_number:
            print("you guessed too high")
        elif guess < random_number:
            print("you guessed too low")
        elif guess == random_number:
            print("congratulations! you guessed correctly")
            break
number_guessing_game()