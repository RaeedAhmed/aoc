from collections import deque
from functools import partial

from aoc.utils import Session, profiler


@profiler
def solution(marker_length: int, data: deque[str]) -> int:
    buffer, count = deque(), marker_length
    for _ in range(marker_length):
        buffer.append(data.popleft())
    while data:
        if len(set(buffer)) == marker_length:
            return count
        buffer.popleft()
        buffer.append(data.popleft())
        count += 1


part1 = partial(solution, 4)
part2 = partial(solution, 14)


def main():
    data = Session().load_data()
    [print(f(deque(data))) for f in (part1, part2)]


if __name__ == "__main__":
    main()
