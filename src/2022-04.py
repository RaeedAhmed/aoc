import re
from functools import partial
from typing import Callable

from aoc.utils import Session, profiler


@profiler
def solution(func: Callable[[set, set], bool], data: str) -> int:
    sections = re.compile(r"(\d+)-(\d+)\,(\d+)-(\d+)")

    def condition(row: str) -> bool:
        a, b, c, d = map(int, sections.match(row).groups())
        return func(set(range(a, b + 1)), set(range(c, d + 1)))

    return sum(map(condition, data.splitlines()))


part1 = partial(solution, lambda a, b: a.issuperset(b) or b.issuperset(a))
part2 = partial(solution, lambda a, b: bool(a.intersection(b)))


def main():
    data = Session().load_data()
    [print(f(data)) for f in (part1, part2)]


if __name__ == "__main__":
    main()
