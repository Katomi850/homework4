import unittest
from edde import check_age

class My_Test(unittest.TestCase):
    def test_valid_age(self):
        self.assertEqual(check_age(18), "Ви можете використовувати цей сервіс")
        self.assertEqual(check_age(25), "Ви можете використовувати цей сервіс")

    def test_invalid_age(self):
        self.assertEqual(check_age(17), "Вам має бути 18 років або більше")
        self.assertEqual(check_age(0), "Вам має бути 18 років або більше")

    def test_edge_case(self):
        self.assertEqual(check_age(18), "Ви можете використовувати цей сервіс")
