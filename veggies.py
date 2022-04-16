veg_dict = {'cabbage': 3.57, 'carrot': 2.99, 'spinach': 4.13, 'asparagus': 3.56, 'artichoke': 4.00, 'lettuce': 3.83}
fruit_dict = {'peach': 0.65, 'banana': 0.23, 'watermelon': 2.45, 'apple': 0.99, 'dragonfruit': 1.23}
store_dict = {**veg_dict, **fruit_dict}

order1 = {'cabbage': 2, 'spinach' : 3, 'artichoke': 5, 'apple': 10, 'banana': 7}

order_total = 0

for item, quantity in order1.items():
    order_total += store_dict[item] * quantity
print(order_total)

