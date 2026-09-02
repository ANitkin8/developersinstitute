#exercise 1
def display_message():
    print("I am learning about functions in Python")
display_message()
#exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("Alice in Wonderland")
#exercise 3
def describe_city(city, country="unknown"):
    print(f"{city} is in {country}")
describe_city("London", "England")
describe_city("Jerusalem", "Israel")
#exercise 4
import random
def pick_number(number):
    if 1<= number <= 100:
        random_number=random.randint(1, 100)
        if number == random_number:
            print("Success! your numbers match")
        else:
            print(f"sorry! Your number: {number}, Random number: {random_number}")

    else:
        print("please enter a number between 1 and 100")
#exercise 5
def make_shirt(size="large", text="I love Python"):
    print(f"the size of the shirt is {size} and the text is {text}")
make_shirt()
make_shirt("medium")
make_shirt("XL", "I love Israel")
#exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for name in magicians:
        print(name)
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = f"{magicians[i]} The Great"

make_great(magician_names)
show_magicians(magician_names)
#exercise 7
def get_random_temp():
    random_temp= random.uniform(-10, 40)
    return random_temp
def main():
        temp = get_random_temp()
        if temp < 0:
            print("Brrr, thats freezing! Wear some extra layers today!")
        elif 0 <= temp <16:
            print("quite chilly! Dont forget your coat")
        elif 16 <= temp <= 23:
            print("nice weather")
        elif 24 <= temp < 32:
            print("A bit warm, stay hydrated")
        else:
            print("Its really hot! Stay cool")
main()
