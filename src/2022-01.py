import heapq
from typing import Iterator

from aoc.utils import Session, profiler


def get_calories(data: str) -> Iterator[int]:
    elves = (items.strip() for items in data.split("\n\n"))
    return (sum((map(int, values.split("\n")))) for values in elves)


@profiler
def part1(calories: Iterator[int]) -> int:
    return max(calories)


@profiler
def part2(calories: Iterator[int]) -> int:
    return sum(heapq.nlargest(3, calories))


@profiler
def part2_sorted(calories: Iterator[int]) -> int:
    return sum(sorted(calories)[-3:])


def main():
    data = Session().load_data()
    [print(f(get_calories(data))) for f in (part1, part2, part2_sorted)]


if __name__ == "__main__":
    main()
