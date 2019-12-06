import random


class Product():
    '''
    Acme Inc. products class
    '''
    def __init__(self, name=None, price=10, weight=20, flammability=0.5,
                 identifier=None):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        steal = self.price / self.weight
        if steal < 0.5:
            return 'Not so stealable...'
        elif steal >= 0.5 and steal < 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        expl = self.flammability * self.weight
        if expl < 10:
            return '...fizzle.'
        elif expl >= 10 and expl < 50:
            return '...boom!'
        else:
            return 'BABOOM!'


class BoxingGlove(Product):
    '''
    Boxing glove class
    '''
    def __init__(self, name=None, price=10, weight=10, flammability=0.5,
                 identifier=None):
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def explode(self):
        print('...it\'s a glove.')

    def punch(self):
        wei = self.weight
        if wei < 5:
            print('That tickles.')
        elif wei >= 5 and wei < 15:
            print('Hey that hurt!')
        else:
            print('OUCH!')
