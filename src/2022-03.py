import string
from functools import reduce

from aoc.utils import Session, profiler

priority = {char: index + 1 for index, char in enumerate(string.ascii_letters)}


def compartments(rucksack: str) -> tuple[str]:
    l = len(rucksack) // 2
    return rucksack[:l], rucksack[l:]


def common(compartments: tuple[str]) -> str:
    return reduce(lambda a, b: set(a).intersection(set(b)), compartments).pop()


@profiler
def part1(data: list[str]) -> int:
    return sum((priority[common(compartments(rucksack))] for rucksack in data))


@profiler
def part2(data: list[str]) -> int:
    N = 3
    groups = (data[i : i + N] for i in range(0, len(data), N))
    return sum((priority[common(group)] for group in groups))


def main():
    data = Session().load_data()
    data = [line.strip() for line in data.splitlines()]
    [print(f(data)) for f in (part1, part2)]


if __name__ == "__main__":
    main()
