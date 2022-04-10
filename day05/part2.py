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
        # process parameters
        de = int(code[3:])
        c = int(code[2])
        b = int(code[1])
        a = int(code[0])
        if de == 99:
            return program
        print("===================")
        print(f"Pointer: {cc}")
        first_param = program[cc + 1]
        second_param = program[cc + 2]
        third_param = program[cc + 3]
        print(f"IntCode: {code}, 1st param: {first_param}, 2nd param: {second_param},"
              f" 3rd param: {third_param}")
        # process immediate mode
        if de == 1:
            if c == 0:
                first_param = program[first_param]
            if b == 0:
                second_param = program[second_param]
            program[third_param] = first_param + second_param
            cc += 4
        elif de == 2:
            if c == 0:
                first_param = program[first_param]
            if b == 0:
                second_param = program[second_param]
            program[third_param] = first_param * second_param
            cc += 4
        elif de == 3:
            # cannot be in immediate mode
            user_input = int(input("Provide an input:"))
            program[first_param] = user_input
            print(f"Writing {user_input} to position {first_param}")
            cc += 2
        elif de == 4:
            # can be in immediate mode
            if c == 0:
                first_param = program[first_param]
            print(first_param)
            cc += 2
        elif de == 5:
            # can be in immediate mode
            if c == 0:
                first_param = program[first_param]
            if b == 0:
                second_param = program[second_param]
            if first_param != 0:
                cc = second_param
                print(f"Setting instruction pointer to {cc}")
            else:
                cc += 3
        elif de == 6:
            if c == 0:
                first_param = program[first_param]
            if b == 0:
                second_param = program[second_param]
            if first_param == 0:
                cc = second_param
            else:
                cc += 3
        elif de == 7:
            if c == 0:
                first_param = program[first_param]
            if b == 0:
                second_param = program[second_param]
            if first_param < second_param:
                program[third_param] = 1
            else:
                program[third_param] = 0
            cc += 4
        elif de == 8:
            if c == 0:
                first_param = program[first_param]
            if b == 0:
                second_param = program[second_param]
            if first_param == second_param:
                program[third_param] = 1
                print(f"Storing 1 in position {third_param}")
            else:
                program[third_param] = 0
                print(f"Storing 0 in position {third_param}")
            cc += 4


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file')
    args = parser.parse_args()
    with open(args.data_file) as f:
        compute(f.read())
    return 0


if __name__ == '__main__':
    exit(main())
