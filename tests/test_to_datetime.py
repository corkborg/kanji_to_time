
from datetime import datetime, timedelta
import unittest
from unittest.mock import patch, MagicMock, Mock
from kanji_to_time import to_datetime

class TestClass(unittest.TestCase):

    def test_standard(self):
        dt = to_datetime("2024年4月5日22時30分4秒")
        self.assertEqual(dt, datetime(year=2024, month=4, day=5, hour=22, minute=30, second=4))

        dt = to_datetime("２０２０年５月７日")
        self.assertEqual(dt, datetime(year=2020, month=5, day=7))

        dt = to_datetime("二〇二五年十二月七日")
        self.assertEqual(dt, datetime(year=2025, month=12, day=7))

        dt = to_datetime("二千年八月三日")
        self.assertEqual(dt, datetime(year=2000, month=8, day=3))

        dt = to_datetime("弐零弐参年伍月肆日")
        self.assertEqual(dt, datetime(year=2023, month=5, day=4))


    def test_detail(self):
        dt = to_datetime("2024年四月5日")
        self.assertEqual(dt, datetime(year=2024, month=4, day=5))

        dt = to_datetime("２０２4年４月5日")
        self.assertEqual(dt, datetime(year=2024, month=4, day=5))
