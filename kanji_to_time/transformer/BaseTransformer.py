from lark import Token, Transformer
from .. import convert_table

class BaseTransformer(Transformer):
    """
    timedelta, datetime共通の解析ルール
    """

    def kanji_digit(self, args: list[Token]):
        return convert_table.to_number(args[0].value)

    def zenkaku_digit(self, args: list[Token]):
        return convert_table.to_number(args[0].value)

    def number(self, args):
       if args[0] == "-":
            return args[1] * -1
       return args[0]

    def signed(self, args):
        return "-"

    def mixed_number(self, args):
        # 桁をあわせて結合
        strs = [str(arg) for arg in args]
        return int(''.join(strs))

    def kanji_num_parser(self, args):
        return sum(args)

    def unit_juu(self, args):
        if len(args) == 1:
            return int(args[0]) * 10
        return 10

    def unit_sen(self, args):
        if len(args) == 1:
            return int(args[0]) * 1000
        return 1000

    def unit_man(self, args):
        if len(args) == 1:
            return int(args[0]) * 10_000
        return 1000

    def unit_oku(self, args):
        if len(args) == 1:
            return int(args[0]) * 100_000_000
        return 1000



