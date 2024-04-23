from datetime import timedelta
from typing import cast
from lark import Tree, Token
from .BaseTransformer import BaseTransformer


class TimeDeltaTransformer(BaseTransformer):
    """
    Datetime生成のための解析ルール
    """

    def start_timedelta(self, args: list[Tree | Token]):
        temp_td = timedelta()
        for arg in args:
            if isinstance(arg, Token):
                if arg.type == "BEFORE_TIME":
                    temp_td *= -1
            else:
                num = cast(int, arg.children[0])
                if arg.data == "duration_day":
                    temp_td += timedelta(days=num)
                elif arg.data == "duration_hour":
                    temp_td += timedelta(hours=num)
                elif arg.data == "duration_minute":
                    temp_td += timedelta(minutes=num)
                elif arg.data == "duration_second":
                    temp_td += timedelta(seconds=num)
        return temp_td
