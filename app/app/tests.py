from django.test import SimpleTestCase

from app import calc


class SimpleCalcTest(SimpleTestCase):

    def test_add(self):
        res = calc.SimpleCalc(5, 5)

        self.assertEqual(res, 10)

    def test_sub(self):
        res = calc.sub(5, 2)

        self.assertEqual(res, 3)
