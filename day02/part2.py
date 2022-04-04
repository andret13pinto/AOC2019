"""
Name : template.py.py
Author : André Pinto
Contact : andret13pinto@hotmail.com
Time    : 04/04/2022 09:16
Desc: From https://github.com/anthonywritescode/aoc2019/blob/master/day00/template.py
"""

import argparse

import pytest

from typing import List
#from support import timing


def compute(s: str, noun: int, verb: int) -> List[int]:
    program = [int(n) for n in s.strip().split(',')]
    program[1] = noun
    program[2] = verb
    cc = 0
    while True:
        code = program[cc]
        if code == 99:
            return program
        elif code == 1:
            program[program[cc + 3]] = program[program[cc + 1]] + program[program[cc + 2]]
        elif code == 2:
            program[program[cc + 3]] = program[program[cc + 1]] * program[program[cc + 2]]
        cc += 4


def modify_input(s: str) -> int:
    for noun in range(100):
        for verb in range(100):
            if compute(s, noun, verb)[0] == 19690720:
                return 100 * noun + verb
    raise AssertionError(f'Unreachable')



@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
            ('1, 0, 0, 0, 99', [2, 0, 0, 0, 99]),
            ('2, 3, 0, 3, 99', [2, 3, 0, 6, 99]),
            ('2, 4, 4, 5, 99, 0', [2, 4, 4, 5, 99, 9801]),
            ('1, 1, 1, 4, 99, 5, 6, 0, 99', [30, 1, 1, 4, 2, 5, 6, 0, 99])
    ),
)
def test(input_s: str, expected: List[int]) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(modify_input(f.read()))
    return 0


if __name__ == '__main__':
    exit(main())
