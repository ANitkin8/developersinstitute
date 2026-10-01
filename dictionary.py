#exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = dict(zip(keys, values))
print(my_dict)

#exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
indv_cost = []


for key, value in family.items():
    if value > 12:
        indv_cost.append(15)
    elif 3 <= value <= 12:
        indv_cost.append(10)
    else :
        indv_cost.append(0)

updated_family = dict(zip(family.keys(), indv_cost))

for key, value in updated_family.items():
    print(f"{key} costs {value} dollars")
total_cost = sum(indv_cost)
print(f"the total cost is {total_cost} dollars")

#exercise 3
zara = {'name': 'Zara',
'creation_date': 1975,
'creator_name': 'Amancio Ortega Gaona',
'type_of_clothes': ['men', 'women', 'children', 'home'],
'international_competitors': ['Gap', 'H&M', 'Benetton'],
'number_stores': 7000,
'major_color':{
'France': 'blue',
    'Spain': 'red',
    'US': 'pink, green'}
}
zara['number_stores']=2
print(f"Zara has clothes for everybody with categories {zara['type_of_clothes']}")
zara.update({'country_creation': 'Spain'})
print (zara["international_competitors"][2])
print(zara['major_color']['US'])
key_count = len(zara)
print(f"There are {key_count} keys in Zara")
for key in zara:
    print(key)

#exercise 4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
result = {item: i for i, item in enumerate(users)}
print(result)
dict_users = {i: user for i, user in enumerate(users)}
print(dict_users)
charmap = {char: i for i, char in enumerate(sorted(users))}
print(charmap)