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
    print("Average weight: ", sum(Product.weight for Product in products)/float(len(products)))
    print("Average price: ", sum(Product.price for Product in products)/float(len(products)))
    print("Average flammability: ", sum(Product.flammability for Product in products)/float(len(products)))


if __name__ == '__main__':
    inventory_report(generate_products())
