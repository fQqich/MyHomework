def read_magic_number(path: str) -> bool:
    with open(path, encoding='utf-8', mode='r') as file:
        row = file.readline()
        try:
            row = int(row)
            return row >= 1 and row < 3
        except ValueError as e:
            print(e)