"""
Name : template.py.py
Author : André Pinto
Contact : andret13pinto@hotmail.com
Time    : 04/04/2022 09:16
Desc: From https://github.com/anthonywritescode/aoc2019/blob/master/day00/template.py
"""

import argparse

import pytest


def compute(s: str) -> int:
    total = 0
    for line in s.splitlines():
        line_val = int(line)
        total += line_val // 3 - 2
    # TODO: implement solution here!
    return total


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            ('12', 2),
            ('14', 2),
            ('1969', 654),
            ('100756', 33583)
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    exit(main())
