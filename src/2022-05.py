import re
from collections import defaultdict, deque
from functools import partial
from typing import Callable, Iterator, NamedTuple

from aoc.utils import Session, profiler

Stack = deque[str]
Stacks = dict[int, Stack]
File = deque[str]


class Move(NamedTuple):
    quantity: int
    origin: int
    destination: int


def parse_stacks(file: File) -> tuple[Stacks, File]:
    box = re.compile(r"[A-Z]")
    stacks: Stacks = defaultdict(deque)
    while file:
        row = file.popleft()
        if not (boxes := list(box.finditer(row))):
            break
        for b in boxes:
            index = b.start()
            stacks[1 + index // 4].appendleft(b.group())
    return stacks, file


def parse_moves(file: File) -> Iterator[Move]:
    values = re.compile(r"(\d+) from (\d+) to (\d+)")
    return (
        Move(*map(int, match.groups()))
        for line in file
        if (match := values.search(line))
    )


def move(stacks: Stacks, moves: Iterator[Move], chunk: bool) -> Stacks:
    for move in moves:
        buffer = deque()
        for _ in range(min(move.quantity, len(stacks[move.origin]))):
            buffer.append(stacks[move.origin].pop())
        if chunk:
            buffer.reverse()
        stacks[move.destination].extend(buffer)
    return stacks


@profiler
def solution(chunk: bool, data: str) -> str:
    file = deque(data.splitlines())
    stacks, file = parse_stacks(file)
    moves = parse_moves(file)
    stacks = move(stacks, moves, chunk)
    return "".join(stacks[key][-1] for key in sorted(stacks.keys()))


part1 = partial(solution, False)
part2 = partial(solution, True)


def main():
    data = Session().load_data()
    [print(f(data)) for f in (part1, part2)]


if __name__ == "__main__":
    main()
