from collections import deque
from functools import partial

from aoc.utils import Session, profiler


@profiler
def solution(n: int, data: str) -> int:
    return next(i for i in range(n, len(data)) if len(set(data[i - n : i])) == n)


part1 = partial(solution, 4)
part2 = partial(solution, 14)


def main():
    data = Session().load_data()
    [print(f(data)) for f in (part1, part2)]


if __name__ == "__main__":
    main()
