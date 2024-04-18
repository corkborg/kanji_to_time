from datetime import datetime
from lark import Tree
from .BaseTransformer import BaseTransformer


class DatetimeTransformer(BaseTransformer):
    """
    Datetime生成のための解析ルール
    """

    def start_datetime(self, args: list[Tree]):
        datetime_args = {}
        for tree in args:
            if tree.data == "year":
                datetime_args["year"] = tree.children[0]
            elif tree.data == "month":
                datetime_args["month"] = tree.children[0]
            elif tree.data == "day":
                datetime_args["day"] = tree.children[0]
            elif tree.data == "hour":
                datetime_args["hour"] = tree.children[0]
            elif tree.data == "minute":
                datetime_args["minute"] = tree.children[0]
            elif tree.data == "second":
                datetime_args["second"] = tree.children[0]

        return datetime(**datetime_args)
