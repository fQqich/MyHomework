from typing import List, Generator


def fizzbuzz(n: int):
    for i in range(1, n + 1):
        if i % 15 == 0:
            yield 'fizzbuzz'
        elif i % 3 == 0:
            yield 'fizz'
        elif i % 5 == 0:
            yield 'buzz'
        else:
            yield str(i)