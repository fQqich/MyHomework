from collections import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    i = 0
    if len(data) < 3:  # Check that the sequence is not less than two values
        return False

    if data[-3] + data[-2] != data[-1]:  # Check that the outermost 3 elements belong to the Fibonacci sequence
        return False

    while data[i] + data[i + 1] != data[-1]:  # The cycle goes on until all elements are checked
        if data[i] + data[i + 1] == data[i + 2]:  # Checking each element for membership in a Fibonacci sequence
            i += 1
        else:
            return False

    return True