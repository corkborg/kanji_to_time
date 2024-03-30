
from datetime import timedelta
import unittest
from unittest.mock import patch, MagicMock, Mock
from kanji_to_time import to_timedelta

class TestClass(unittest.TestCase):
    def test_standard(self):
        td = to_timedelta("二時間三十秒")
        self.assertEqual(td, timedelta(hours=2, seconds=30))

        td = to_timedelta("六日間二時間五分間三秒間")
        self.assertEqual(td, timedelta(days=6, hours=2, minutes=5, seconds=3))

        td = to_timedelta("六日二時五分三秒")
        self.assertEqual(td, timedelta(days=6, hours=2, minutes=5, seconds=3))

        td = to_timedelta("90秒")
        self.assertEqual(td, timedelta(seconds=90))

        td = to_timedelta("マイナス七億分")
        self.assertEqual(td, timedelta(minutes=-700_000_000))

    def test_detail(self):
        td = to_timedelta("二時３分")
        self.assertEqual(td, timedelta(hours=2, minutes=3))

        td = to_timedelta("二時三分四秒")
        self.assertEqual(td, timedelta(hours=2, minutes=3, seconds=4))

        td = to_timedelta("二9３分")
        self.assertEqual(td, timedelta(minutes=293))

        td = to_timedelta("二十分")
        self.assertEqual(td, timedelta(minutes=20))

        td = to_timedelta("千二十分")
        self.assertEqual(td, timedelta(minutes=1020))

        td = to_timedelta("１億千二十分")
        self.assertEqual(td, timedelta(minutes=100_001_020))

        td = to_timedelta("5万千二十分")
        self.assertEqual(td, timedelta(minutes=51_020))

        td = to_timedelta("六億二十分")
        self.assertEqual(td, timedelta(minutes=600_000_020))

        td = to_timedelta("5千二十分")
        self.assertEqual(td, timedelta(minutes=5020))

        td = to_timedelta("-二分")
        self.assertEqual(td, timedelta(minutes=-2))

        td = to_timedelta("マイナス二分")
        self.assertEqual(td, timedelta(minutes=-2))