class Suppressor:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type in self.exceptions:
            return True


with Suppressor(ZeroDivisionError):
    1 / 0
print("This line is executed")

from contextlib import contextmanager


@contextmanager
def suppressor(*exceptions):
    try:
        yield
    except exceptions:
        pass


with suppressor(ZeroDivisionError):
    1 / 0
print("This line is executed")