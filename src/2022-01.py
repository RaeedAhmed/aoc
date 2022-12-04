import heapq

from aoc.utils import Session, profiler


@profiler
def part1(data: str) -> int:
    elves = (items.strip() for items in data.split("\n\n"))
    calories = (sum((map(int, values.split("\n")))) for values in elves)
    return max(calories)


@profiler
def part2(data) -> int:
    elves = (items.strip() for items in data.split("\n\n"))
    calories = (sum((map(int, values.split("\n")))) for values in elves)
    return sum(heapq.nlargest(3, calories))


@profiler
def part2_sorted(data) -> int:
    elves = (items.strip() for items in data.split("\n\n"))
    calories = (sum((map(int, values.split("\n")))) for values in elves)
    return sum(sorted(calories)[-3:])


def main():
    data = Session().load_data()
    [print(f(data)) for f in (part1, part2, part2_sorted)]


if __name__ == "__main__":
    main()
