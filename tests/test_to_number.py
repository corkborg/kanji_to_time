import unittest
import kanji_to_time as ktt


class TestClass(unittest.TestCase):
    def test01(self):
        n = ktt.to_number("2024")
        self.assertEqual(n, 2024)

        n = ktt.to_number("二四")
        self.assertEqual(n, 24)

        n = ktt.to_number("２３")
        self.assertEqual(n, 23)

        n = ktt.to_number("弐壱")
        self.assertEqual(n, 21)

        n = ktt.to_number("マイナス四３2")
        self.assertEqual(n, -432)

        n = ktt.to_number("ひく43")
        self.assertEqual(n, -43)

        n = ktt.to_number("+3")
        self.assertEqual(n, 3)

        n = ktt.to_number("プラス9")
        self.assertEqual(n, 9)

        n = ktt.to_number("9")
        self.assertEqual(n, 9)

        n = ktt.to_number("四")
        self.assertEqual(n, 4)

        n = ktt.to_number("〇")
        self.assertEqual(n, 0)

        n = ktt.to_number("○")
        self.assertEqual(n, 0)

        n = ktt.to_number("◯")
        self.assertEqual(n, 0)

        n = ktt.to_number("３")
        self.assertEqual(n, 3)

        n = ktt.to_number("-３")
        self.assertEqual(n, -3)

        n = ktt.to_number("九十九")
        self.assertEqual(n, 99)

        n = ktt.to_number("十九")
        self.assertEqual(n, 19)

        n = ktt.to_number("千7")
        self.assertEqual(n, 1007)

        n = ktt.to_number("百")
        self.assertEqual(n, 100)

        n = ktt.to_number("5百")
        self.assertEqual(n, 500)

        n = ktt.to_number("２万千7")
        self.assertEqual(n, 21007)

        n = ktt.to_number("2億千7")
        self.assertEqual(n, 200_001_007)

        n = ktt.to_number("200,001,007")
        self.assertEqual(n, 200_001_007)

        n = ktt.to_number("２萬七阡佰４拾")
        self.assertEqual(n, 27140)
