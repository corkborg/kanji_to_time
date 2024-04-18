def to_number(char: str) -> int:
    """
    数字に変換する

    :param char: 変換対象の一文字
    """
    return table[char]


zenkaku_table = {
    "０": 0,
    "１": 1,
    "２": 2,
    "３": 3,
    "４": 4,
    "５": 5,
    "６": 6,
    "７": 7,
    "８": 8,
    "９": 9,
}

zero_table = {
    "零": 0,
    "ゼロ": 0,
    "〇": 0,
    "○": 0,  # 誤りのゼロ
    "◯": 0,  # 誤りのゼロ
}

ascii_number = {str(num): num for num in range(0, 10)}

table = {
    "一": 1,
    "壱": 1,
    "二": 2,
    "弐": 2,
    "三": 3,
    "参": 3,
    "四": 4,
    "肆": 4,
    "五": 5,
    "伍": 5,
    "六": 6,
    "陸": 6,
    "七": 7,
    "漆": 7,
    "八": 8,
    "捌": 8,
    "九": 9,
    "玖": 9,
    **zenkaku_table,
    **zero_table,
    **ascii_number,
}
