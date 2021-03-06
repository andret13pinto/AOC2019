"""
Name : template.py.py
Author : André Pinto
Contact : andret13pinto@hotmail.com
Time    : 04/04/2022 09:16
Desc: From https://github.com/anthonywritescode/aoc2019/blob/master/day00/template.py
"""

import argparse
import pytest
from typing import Dict, NamedTuple


class Node(NamedTuple):
    parent: str
    name: str


def read_map(s: str):
    node_dict: Dict[str, NamedTuple] = {'COM': Node('', 'COM')}
    for line in s.splitlines():
        parent, child = line.strip().split(')')
        node_dict[child] = Node(parent, child)
    return node_dict

    
def compute(s: str) -> int:
    node_dict = read_map(s)
    final_sum = 0
    for _, node in node_dict.items():
        while node.name != 'COM':
            final_sum += 1
            node = node_dict[node.parent]
    return final_sum


test_string = "COM)B\n B)C\n C)D\n D)E\n E)F\n B)G\n G)H\n D)I\n E)J\n J)K\n K)L"


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (test_string, 42),
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
