from functools import partial
from typing import Callable

from aoc.utils import Session, profiler


def section(assignment: str) -> set[int]:
    bounds = tuple(int(num) for num in assignment.split("-"))
    return set(range(bounds[0], bounds[1] + 1))


def condition(func: Callable, pair: str) -> bool:
    a, b = (section(x) for x in pair.split(","))
    return func(a, b)


contains = partial(condition, lambda a, b: a.issuperset(b) or b.issuperset(a))
overlap = partial(condition, lambda a, b: bool(a.intersection(b)))


@profiler
def part(condition: Callable, data: list[str]) -> int:
    return sum((condition(pair) for pair in data))


part1 = partial(part, contains)
part2 = partial(part, overlap)


def main():
    data = Session().load_data()
    [print(f(data.splitlines())) for f in (part1, part2)]


if __name__ == "__main__":
    main()
