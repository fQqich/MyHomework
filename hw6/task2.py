def backspace_compare(first: str, second: str):
    def process_string(s: str) -> str:
        stack = []
        for char in s:
            if char == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

    return process_string(first) == process_string(second)