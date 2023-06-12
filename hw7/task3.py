from pathlib import Path
from typing import Optional, Callable


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    count = 0
    for file_path in dir_path.glob(f"*.{file_extension}"):
        with open(file_path, "r") as file:
            if tokenizer is None:
                count += sum(1 for _ in file)
            else:
                count += sum(len(tokenizer(line)) for line in file)
    return count