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


def move_one(stacks: Stacks, moves: Iterator[Move]) -> Stacks:
    for move in moves:
        for _ in range(min(move.quantity, len(stacks[move.origin]))):
            stacks[move.destination].append(stacks[move.origin].pop())
    return stacks


def move_chunk(stacks: Stacks, moves: Iterator[Move]) -> Stacks:
    for move in moves:
        chunk = deque()
        for _ in range(min(move.quantity, len(stacks[move.origin]))):
            chunk.appendleft(stacks[move.origin].pop())
        stacks[move.destination].extend(chunk)
    return stacks


@profiler
def solution(crane_move: Callable[[Stacks, Iterator[Move]], Stacks], data: str) -> str:
    file = deque(data.splitlines())
    stacks, file = parse_stacks(file)
    moves = parse_moves(file)
    stacks = crane_move(stacks, moves)
    return "".join(stacks[key][-1] for key in sorted(stacks.keys()))


part1 = partial(solution, move_one)
part2 = partial(solution, move_chunk)


def main():
    data = Session().load_data()
    [print(f(data)) for f in (part1, part2)]


if __name__ == "__main__":
    main()
