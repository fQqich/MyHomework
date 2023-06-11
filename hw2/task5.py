import string


def custom_range(iterable, start, stop=None, step=1):
    if not stop:
        stop = start
        start = 0
        result = []
        i = 0
        while start != iterable.index(stop):
            if i % abs(step) == 0:
                result.append(iterable[start])
            if step > 0:
                start += 1
            else:
                start -= 1
            i += 1
        return result
    result = []
    i = 0
    while iterable.index(start) != iterable.index(stop):
        if i % abs(step) == 0:
            result.append(iterable[iterable.index(start)])
        if step > 0:
            index = iterable.index(start)
            index += 1
            start = iterable[index]

        else:
            index = iterable.index(start)
            index -= 1
            start = iterable[index]

        i += 1
    return result