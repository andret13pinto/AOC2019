"""
Name : template.py.py
Author : André Pinto
Contact : andret13pinto@hotmail.com
Time    : 04/04/2022 09:16
Desc: From https://github.com/anthonywritescode/aoc2019/blob/master/day00/template.py
"""

import argparse
import pytest
from itertools import groupby


def is_p_valid(p_string: str) -> int:
    digit_groups = groupby(p_string)
    last_digit = -1
    flag = False
    for digit, group in digit_groups:
        if int(digit) >= last_digit:
            last_digit = int(digit)
        else:
            return 0
        if len(list(group)) == 2:
            flag = True
    if flag:
        return 1
    return 0


def compute() -> int:
    p_count = 0
    for p in range(172851, 675870):
        p_string = str(p)
        p_count += is_p_valid(p_string)
    return p_count


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            ('112233', 1),
            ('123444', 0),
            ('111122', 1),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert is_p_valid(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    #parser.add_argument('data_file')
    args = parser.parse_args()
    print(compute())
    return 0


if __name__ == '__main__':
    exit(main())
