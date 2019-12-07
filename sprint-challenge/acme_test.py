#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.5)

    def test_steal_method(self):
        alpha = Product(price=20, weight=20)
        self.assertEqual(alpha.stealability(), 'Very stealable!')

    def test_explode_method(self):
        beta = Product(flammability=2, weight=50)
        self.assertEqual(beta.explode(), 'BABOOM!')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        gamma = generate_products()
        self.assertEqual(len(set(gamma)), 30)

    def test_legal_names(self):
        delta = generate_products()
        theta = ADJECTIVES + NOUNS
        self.assertIn(delta, theta)

if __name__ == '__main__':
    unittest.main()
