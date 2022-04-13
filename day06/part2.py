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


def read_map(s: str) -> Dict:
    node_dict: Dict[str, NamedTuple] = {'COM': Node('', 'COM')}
    for line in s.splitlines():
        parent, child = line.strip().split(')')
        node_dict[child] = Node(parent, child)
    return node_dict


def compute(s: str) -> int:
    nodes = read_map(s)
    node = nodes['YOU']
    me_path = {}
    hops = 0
    while node.name != 'COM':
        me_path[node.name] = hops
        node = nodes[node.parent]
        hops += 1
    node = nodes['SAN']
    hops = 0
    san_path = {}
    while node.name != 'COM':
        san_path[node.name] = hops
        node = nodes[node.parent]
        hops += 1
    candidates = {node: hops for node, hops in me_path.items() if node in san_path.keys()}
    min_node = min(candidates, key=candidates.get)
    print(san_path[min_node], me_path[min_node])
    return san_path[min_node] + me_path[min_node] - 2


test_string = "COM)B\n B)C\n C)D\n D)E\n E)F\n B)G\n G)H\n D)I\n E)J\n J)K\n K)L\n K)YOU\n I)SAN"


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (test_string, 4),
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
