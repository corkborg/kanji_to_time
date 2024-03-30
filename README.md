# Kanji to time

日本語の漢字などで書かれた年月日をPythonのdatetime型やtimedelta型に変換するライブラリ。<br/>

漢数字、旧字漢数字、全角などに対応しています。

## 使い方

```bash
pip install kanji_to_time
```

```python
import kanji_to_time as ktt

text = "2024年4月5日22時30分4秒"
dt = ktt.to_datetime(text)
print(dt)

text = "二時間三十秒"
td = ktt.to_timedelta(text)
print(td)
```

## 対応パターン例

### datetimeの変換

```python
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
```

### timedeltaの変換

```python
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
```

その他詳細なパターンはこちらのファイルを参照
[tests/test_to_datetime.py](tests/test_to_datetime.py)<br/>
[tests/test_to_timedelta.py](tests/test_to_datetime.py)<br/>
[tests/test_to_number.py](tests/test_to_datetime.py)<br/>

## ユニットテスト

```
pip install -r requirements.txt
python -m unittest discover -s tests
```

## 問い合わせ

バグや機能要望についてはissueに報告をお願いします。
https://github.com/corkborg/kanji_to_time/issues

その他の問い合わせはメールまで（メール転送サービスを利用しています）<br/>
ax4squil8&#064;mozmail.com