from datetime import timedelta
from lark import Tree
from .BaseTransformer import BaseTransformer

class TimeDeltaTransformer(BaseTransformer):
    """
    Datetime生成のための解析ルール
    """

    def start_timedelta(self, args: list[Tree]):
        datetime_args = {}
        minus = False
        for tree in args:
            if tree.data == "duration_day":
                datetime_args["days"] = tree.children[0]
            elif tree.data == "duration_hour":
                datetime_args["hours"] = tree.children[0]
            elif tree.data == "duration_minute":
                datetime_args["minutes"] = tree.children[0]
            elif tree.data == "duration_second":
                datetime_args["seconds"] = tree.children[0]
            elif tree.data == "before_time":
                minus = True
            # elif tree.data == "after_time":  # ignore
            #    minus = False
        if minus:
            return timedelta(**datetime_args) * -1
        return timedelta(**datetime_args)