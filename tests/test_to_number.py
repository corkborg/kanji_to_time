from datetime import datetime, timedelta
import unittest
from unittest.mock import patch, MagicMock, Mock
from kanji_to_time import to_number

class TestClass(unittest.TestCase):
    def test01(self):
        n = to_number('2024')
        self.assertEqual(n, 2024)

        n = to_number('二四')
        self.assertEqual(n, 24)

        n = to_number('２３')
        self.assertEqual(n, 23)

        n = to_number('弐壱')
        self.assertEqual(n, 21)

        n = to_number('マイナス四３2')
        self.assertEqual(n, -432)

        n = to_number('9')
        self.assertEqual(n, 9)

        n = to_number('四')
        self.assertEqual(n, 4)

        n = to_number('〇')
        self.assertEqual(n, 0)

        n = to_number('○')
        self.assertEqual(n, 0)

        n = to_number('◯')
        self.assertEqual(n, 0)

        n = to_number('３')
        self.assertEqual(n, 3)

        n = to_number('-３')
        self.assertEqual(n, -3)

        n = to_number('九十九')
        self.assertEqual(n, 99)

        n = to_number('十九')
        self.assertEqual(n, 19)

        n = to_number('千7')
        self.assertEqual(n, 1007)

        n = to_number('２万千7')
        self.assertEqual(n, 21007)

        n = to_number('2億千7')
        self.assertEqual(n, 200_001_007)