"""
Name : template.py.py
Author : André Pinto
Contact : andret13pinto@hotmail.com
Time    : 04/04/2022 09:16
Desc: From https://github.com/anthonywritescode/aoc2019/blob/master/day00/template.py
"""

import argparse
import pytest
from typing import Dict, Set, Optional

node_dict: Dict[str, 'Node'] = {}

class Node:
    def __init__(self, name: str, **kwargs: str) -> None:
        self.name :str = name
        self.parents : Set[str] = set()  
        self.children : Set[str] = set()
        if 'parent' in kwargs:
            self.add_parent(kwargs.get('parent'))
    
    def get_direct_connections(self):
        return len(self.parents)

    def get_indirect_connections(self):
        count = 0
        for parent in self.parents:
            count += node_dict[parent].get_indirect_connections() + node_dict[parent].get_direct_connections()
        return count

    def add_children(self, name: str):
        self.children.add(name)

    def add_parent(self, name: str):
        self.parents.add(name)

    def __repr__(self) -> str:
        return f'Node: {self.name}, with parents {self.parents} and children {self.children}. '

def read_map(s: str):
    for line in s.splitlines():
        first_key, second_key = line.strip().split(')')
        if first_key not in node_dict.keys():
            node_dict[first_key] = Node(first_key)
        node_dict[first_key].add_children(second_key)
        if second_key not in node_dict.keys():
            node_dict[second_key] = Node(second_key, parent = first_key)
        else:
            node_dict[second_key].add_parent(first_key)
    return node_dict

    
def compute(s: str) -> int:
    node_dict = read_map(s)
    final_sum = 0
    for _, node in node_dict.items():
        final_sum += node.get_direct_connections() +  node.get_indirect_connections()
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
