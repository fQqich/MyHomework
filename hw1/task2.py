from typing import Tuple

def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open('numbers.txt') as fi:
        for line in fi: #we use this construction to read the first line in the file
            data = [int(x) for x in line.split(",")]  #split the string into characters, the separator is a comma
            Minimum = min(data) #using the built-in function to find the minimum
            Maximum = max(data) #using the built-in function to find the maximum
            return [Minimum, Maximum]