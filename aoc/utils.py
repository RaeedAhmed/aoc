import inspect
import os
from functools import wraps
from pathlib import Path
from time import perf_counter as timer
from urllib import request


class Session:
    def __init__(self) -> None:
        # Returns filename stem of top level of stack (calling file) e.g -1
        self.filename = Path(inspect.stack()[-1].filename).stem
        self.year, self.day = map(int, self.filename.split("-"))
        self.url = f"https://adventofcode.com/{self.year}/day/{self.day}/input"

    @property
    def headers(self) -> dict[str]:
        """
        Set environment variable like so:
        export AOC_SESSION="session=<token>"
        """
        return {"Cookie": os.environ.get("AOC_SESSION")}

    def load_data(self) -> str:
        r = request.Request(url=self.url, headers=self.headers)
        return request.urlopen(r).read().decode("utf-8")


def profiler(func):
    @wraps(func)
    def wrapper_profiler(*args, **kwargs):
        tic = timer()
        value = func(*args, **kwargs)
        toc = timer()
        elapsed = (toc - tic) * 1_000
        print(f"{func.__name__!r} took {elapsed:.2f} ms")
        return value

    return wrapper_profiler
