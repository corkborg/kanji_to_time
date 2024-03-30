from datetime import datetime, timedelta
from typing import cast
from pathlib import Path
from lark import Lark

from .transformer.DatetimeTransformer import DatetimeTransformer
from .transformer.TimedeltaTransformer import TimeDeltaTransformer

schema_path = Path(__file__).parent / 'grammer'/ 'kanji_to_time.lark'

def to_datetime(text: str) -> datetime:
    """
    文字列をdatetimeに変換する
    """
    parser = Lark.open(
        str(schema_path),
        start=['start_datetime'],
        parser='lalr',
        transformer=DatetimeTransformer()
    )
    return cast(datetime, parser.parse(text, start='start_datetime'))

def to_timedelta(text: str) -> timedelta:
    """
    文字列をtimedeltaに変換する
    """
    parser = Lark.open(
        str(schema_path),
        start=['start_timedelta'],
        parser='lalr',
        transformer=TimeDeltaTransformer()
    )
    return cast(timedelta, parser.parse(text, start='start_timedelta'))

def to_number(text: str) -> timedelta:
    """
    数値に変換する。主にデバッグ用の関数
    """
    parser = Lark.open(
        str(schema_path),
        start=['number'],
        parser='lalr',
        transformer=TimeDeltaTransformer()
    )
    return cast(timedelta, parser.parse(text, start='number'))

