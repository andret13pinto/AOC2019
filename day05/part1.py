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

'''
Opcode 3 takes a single integer as input and saves it to the position given by its only parameter.
For example, the instruction 3,50 would take an input value and store it at address 50.

Opcode 4 outputs the value of its only parameter.
For example, the instruction 4,50 would output the value at address 50.
'''


def compute(s: str) -> List[int]:
    program = [int(n) for n in s.strip().split(',')]
    cc = 0
    while True:
        code = str(program[cc])
        code = code.zfill(5)
        print(code)
        first_param = program[cc + 1]
        second_param = program[cc + 2]
        third_param = program[cc + 3]
        increment = 4
        # process parameters
        de = int(code[3:])
        c = int(code[2])
        b = int(code[1])
        a = int(code[0])
        # process immediate mode
        if de == 99:
            return program
        elif de == 1:
            if c == 0:
                first_param = program[first_param]
            if b == 0:
                second_param = program[second_param]
            program[third_param] = first_param + second_param
        elif de == 2:
            if c == 0:
                first_param = program[first_param]
            if b == 0:
                second_param = program[second_param]
            program[third_param] = first_param * second_param
        elif de == 3:
            # cannot be in immediate mode
            user_input = int(input())
            program[first_param] = user_input
            increment = 2
        elif de == 4:
            # can be in immediate mode
            if c == 0:
                first_param = program[first_param]
            print(first_param)
            increment = 2
        cc += increment


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()
    with open(args.data_file) as f:
        compute(f.read())
    return 0


if __name__ == '__main__':
    exit(main())
