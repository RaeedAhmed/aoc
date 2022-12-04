from dataclasses import dataclass
from functools import partial
from typing import Iterator

from aoc.utils import Session, profiler


@profiler
def func(combinations: list[str], data: list[str]) -> int:
    scoring = {k: v for k, v in zip(combinations, range(1, 10))}
    return sum((scoring[round] for round in data))


part1 = partial(func, ["B X", "C Y", "A Z", "A X", "B Y", "C Z", "C X", "A Y", "B Z"])
part2 = partial(func, ["B X", "C X", "A X", "A Y", "B Y", "C Y", "C Z", "A Z", "B Z"])


def main():
    data = [line.strip() for line in Session().load_data().splitlines()]
    [print(f(data)) for f in (part1, part2)]


if __name__ == "__main__":
    main()
