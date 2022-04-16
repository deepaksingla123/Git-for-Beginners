veg_dict = {'cabbage': 2.87, 'carrot': 1.59, 'spinach': 3.33, 'asparagus': 2.54, 'artichoke': 3.00, 'lettuce': 2.43}

order1 = {'cabbage': 2, 'spinach' : 3, 'artichoke': 5}

order_total = 0

for veggie, quantity in order1.items():
    order_total += veg_dict[veggie] * quantity
print(order_total)

