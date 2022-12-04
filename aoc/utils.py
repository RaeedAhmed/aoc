import inspect
import os
from functools import wraps
from pathlib import Path
from time import perf_counter as timer
from urllib import request


class Session:
    @property
    def headers(self) -> dict[str]:
        """
        Set environment variable like so:
        export AOC_SESSION="session=<token>"
        """
        return {"Cookie": os.environ.get("AOC_SESSION")}

    @property
    def filename(self) -> str:
        """Returns filename stem of top level of stack (calling file) e.g -1"""
        return Path(inspect.stack()[-1].filename).stem

    @property
    def year(self):
        return int(self.filename.split("-")[0])

    @property
    def day(self):
        return int(self.filename.split("-")[1])

    @property
    def url(self) -> str:
        return f"https://adventofcode.com/{self.year}/day/{self.day}/input"

    def load_data(self) -> str:
        r = request.Request(url=self.url, headers=self.headers)
        return request.urlopen(r).read().decode("utf-8")


def profiler(func):
    @wraps(func)
    def wrapper_profiler(*args, **kwargs):
        tic = timer()
        value = func(*args, **kwargs)
        toc = timer()
        elapsed = toc - tic
        print(f"{func.__name__!r} took {elapsed:.6f} s")
        return value

    return wrapper_profiler
