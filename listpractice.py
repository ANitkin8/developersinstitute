#exercise 1
my_fav_numbers = [8, 13, 18]
my_fav_numbers.append(17)
my_fav_numbers.append(33)
my_fav_numbers.pop(4)
friend_fav_numbers = [98, 99, 100]
our_fav_numbers = my_fav_numbers + friend_fav_numbers
#exercise 2
my_tuple = (1+3, 2.5, 'data analysis')
#my_tuple.append('coffee')  this gives an error message
#exercise 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.remove('Blueberries')
basket.append('kiwi')
basket.insert(0, 'Apples')
basket.count("Apples")
basket.clear()
print(basket)
#exercise 4
fruits = []
i = 1
while i<5:
    i += 0.5
    if i.is_integer():
            fruits.append(int(i))
    else:
            fruits.append(i)
print(fruits)
#exercise 5
for num in range(1,21):
    print(num)
#exercise 6
name = input('Enter your name:')
if name.isdigit() or len(name) < 3:
    name = input('give the correct name:')
else:
    print('thank you')
#exercise 7
fav_fruits = []
print('enter your favorite fruits')
fr = input()
fav_fruits.append(fr)
print('name any fruit')
any_fruit = input()
if any_fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
#exercise 8
t=1
while t >0:
    print("choose a topping for your pizza (enter quit at anytime to stop)")
    topping = input()
    if topping != 'quit':
        print(f"Adding {topping} to your pizza.")
        continue
    else:
        break
#exercise 9
ages = []
total_cost=0
print("enter the ages for all of those attending the movie")
user_ages = input()
user_ages.split()
ages = list(map(int, user_ages.split()))
for x in ages:
    if  12>x>3:
        cost = 10
    elif x > 12:
        cost = 15
    else:
        cost = 0
    total_cost += cost
print(f"your total cost is {total_cost}")

