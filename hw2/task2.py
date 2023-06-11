from typing import List, Tuple
from collections import Counter


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    counter = Counter(inp)  #
    rare_letter = min(counter, key=counter.get)
    most_common_letter = max(counter, key=counter.get)
    return most_common_letter, rare_letter