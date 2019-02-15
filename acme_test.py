#!/usr/bin/env python

import unittest
from acme import Product
import acme_report
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_price(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_price(self):
        """Test default product flammbility being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability(self):
        """Test the stealability."""
        prod = Product('Test stealability', 100, 10)
        self.assertEqual(prod.stealability(), 'Very stealable!')

    def test_explode(self):
        """Test the explode method."""
        prod = Product('Test explode', 100, 10, 0.8)
        self.assertEqual(prod.explode(), "...fizzle.")


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_num_products(self):
        """Test default number of products."""
        length_n = len(acme_report.generate_products())
        self.assertEqual(length_n, 30)

    def test_legal_names(self):
        """Test names"""
        for p in acme_report.generate_products():
            a, n = p.name.split()
            self.assertIn(a, ADJECTIVES)
            self.assertIn(n, NOUNS)


if __name__ == '__main__':
    unittest.main()
