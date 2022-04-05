"""
Name : template.py.py
Author : André Pinto
Contact : andret13pinto@hotmail.com
Time    : 04/04/2022 09:16
Desc: From https://github.com/anthonywritescode/aoc2019/blob/master/day00/template.py
"""

import argparse
from typing import List, Tuple

import pytest

def compute_graph(map: List[str]) -> List[Tuple[int]]:
    positions = [(0,0)]
    for step in map:
        orient, distance = step[0], int(step[1:])
        for s in range(distance):
            last_pos = positions[-1]
            if orient == 'R':
                positions.append((last_pos[0] + 1, last_pos[1]))
            if orient == 'L':
                positions.append((last_pos[0] + -1, last_pos[1]))
            if orient == 'U':
                positions.append((last_pos[0], last_pos[1] + 1))
            if orient == 'D':
                positions.append((last_pos[0], last_pos[1] - 1))
    return positions

def find_min_manhattan_distance(list_pos_a: List[Tuple[int]], list_pos_b: List[Tuple[int]]) -> int:
    intersects = set(list_pos_a).intersection(list_pos_b)
    min_distance = 1E10
    for i in intersects:
        if i == (0,0):
            continue
        man_distance = abs(i[0]) + abs(i[1])
        if man_distance < min_distance:
            min_distance = man_distance
    return min_distance

def compute(s: str) -> int:
    w1_map = s.splitlines()[0].strip().split(',')
    w2_map = s.splitlines()[1].strip().split(',')
    w1_positions = compute_graph(w1_map)
    w2_positions = compute_graph(w2_map)
    return find_min_manhattan_distance(w1_positions, w2_positions)


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('R8,U5,L5,D3 \n' 
          'U7,R6,D4,L4', 6),
        ('R75,D30,R83,U83,L12,D49,R71,U7,L7 \n' 
          'U62,R66,U55,R34,D71,R55,D58,R83', 159),
        ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51 \n'
          'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7', 135)
   )
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
