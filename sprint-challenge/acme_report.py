#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        name = str(sample(ADJECTIVES, 1)) + " " + str(sample(NOUNS, 1))
        price = (randint(5, 100))
        weight = (randint(5, 100))
        flammability = (uniform(0.0, 2.5))
        a = Product(name, price, weight, flammability)
        products.append(a)
    return products


def inventory_report(products):
    for Product in products:
        print(Product.name)

    for Product in products:
        print(Product.price)

    for Product in products:
        print(Product.weight)

    for Product in products:
        print(Product.flammability)

#    print(len(set(Product.name)))
#    for Product in products:
#        b = sum(Product.price) / len(Product.price)
#        print(b)
#    for Product in products:
#        print(Product.name)
#    for Product in products:
#        print(sum(Product.price) / len(Product.price))
#    for Product in products:
#        print(sum(Product.weight) / len(Product.weight))
#    for Product in products:
#        print(sum(Product.flammability) / len(Product.flammability))

if __name__ == '__main__':
    inventory_report(generate_products())
