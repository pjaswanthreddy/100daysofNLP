# -*- coding: utf-8 -*-
import random

items = ["bread", "coke", "milk", "eggs", "beer"]

text = ""

for i in range(0, 1000):
    count = random.randint(2, 5)
    order = random.sample(items, count)
    order_str = ','.join(order)

    text += "{}\n".format(order_str)

with open('../../data/processed/grocery.txt', 'w') as f:
    f.write(text)