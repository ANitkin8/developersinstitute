#exercise 1
my_fav_numbers = {8, 13, 18}
my_fav_numbers.add(17)
my_fav_numbers.add(33)
my_fav_numbers.remove(33)
friend_fav_numbers = {98, 99, 100}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

#exercise 2
my_tuple = (1, 5, 8)

#exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.remove('Blueberries')
basket.append('kiwi')
basket.insert(0, 'Apples')
print(basket.count("Apples"))
basket.clear()
print(basket)
#exercise 4
numbers = []
i = 1.5
while i<=5:
    i += 0.5
    if i.is_integer():
            numbers.append(int(i))
    else:
            numbers.append(i)
print(numbers)
#exercise 5
for num in range(1,21):
    print(num)
for num in range(1,21,2):
    print(num)
#exercise 6
while True:
    name = input('Enter your name:')
    if name.isdigit() or len(name)<3:
        print("name must be at least 3 letters and not a number")
    else:
        print('thank you')
        break
#exercise 7
fav_fruits = []
fruits = input('enter your favorite fruits')
fav_fruits = fruits.split()
any_fruit = input('name any fruit')
if any_fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
#exercise 8
toppings = []
t=1
while true:
    topping = input("choose a topping for your pizza (enter quit at anytime to stop)\n")
    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)
        continue
    else:
        break
total_toppings=len(toppings)
cost= 10+2.5*total_toppings
print(toppings)
print(f"your total cost is ${cost}")
#exercise 9
ages = []
total_cost=0
print("enter the ages for all of those attending the movie")
user_ages = input()
user_ages.split()
ages = list(map(int, user_ages.split()))
for x in ages:
    if   3 <= x <= 12:
        cost = 10
    elif x > 12:
        cost = 15
    else:
        cost = 0
    total_cost += cost
print(f"your total cost is {total_cost}")

