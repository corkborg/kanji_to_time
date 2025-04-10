from lark import Token, Transformer
from .. import convert_table


class BaseTransformer(Transformer):
    """
    timedelta, datetime共通の解析ルール
    """

    def number(self, args):
        if isinstance(args[0], Token):
            if args[0].type == "MINUS":
                return args[1] * -1
            elif args[0].type == "PLUS":
                return args[1]
        return args[0]

    def mixed_number(self, args):
        # 桁をあわせて結合
        strs = [str(convert_table.to_number(arg)) for arg in args]
        return int("".join(strs))

    def mixed_number_with_unit(self, args):
        return sum(args)

    def unit_juu(self, args):

        if len(args) == 2:
            return int(args[0]) * 10
        return 10

    def unit_hyaku(self, args):
        if len(args) == 2:
            return int(args[0]) * 100
        return 100

    def unit_sen(self, args):
        if len(args) == 2:
            return int(args[0]) * 1000
        return 1000

    def unit_man(self, args):
        if len(args) == 2:
            return int(args[0]) * 10_000
        return 1000

    def unit_oku(self, args):
        if len(args) == 2:
            return int(args[0]) * 100_000_000
        return 1000
