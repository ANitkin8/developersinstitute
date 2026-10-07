challenge 1

word = input("Enter a word: ")
letter_indices = {}
for index, letter in enumerate(word):
    if letter not in letter_indices:
        #first time seeing this letter, start a new list with the index
        letter_indices[letter] = [index]
    else:
        #character exists: append index to the existing list
        letter_indices[letter].append(index)
print(letter_indices)

#challenge 2
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
basket = []

clean_wallet = wallet.replace("$", "")
#eliminates the dollar sign
new_wallet = int(clean_wallet)
#changes from a string to an integer

for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))
    #cleans the dollar signs and commas of each value in the dictionary and turns the string into an integer
    if  clean_price <= new_wallet:
        basket.append(item)
        new_wallet -= clean_price
if not basket:
    print("nothing")
else:
    basket.sort()
    print(basket)

items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
wallet = "$100"
basket = []

clean_wallet = wallet.replace("$", "")
new_wallet = int(clean_wallet)
for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))
    if  clean_price <= new_wallet:
        basket.append(item)
        new_wallet -= clean_price
if not basket:
    print("nothing")
else:
    basket.sort()
    print(basket)

items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"
basket = []

clean_wallet = wallet.replace("$", "")
new_wallet = int(clean_wallet)
for item, price in items_purchase.items():
    clean_price = int(price.replace("$", "").replace(",", ""))
    if  clean_price <= new_wallet:
        basket.append(item)
        new_wallet -= clean_price
if not basket:
    print("nothing")
else:
    basket.sort()
    print(basket)
