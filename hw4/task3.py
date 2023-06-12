import sys


def my_precious_logger(text: str):
    if text.startswith("error"):  # Checking if a string starts with "error"
        print(text, file=sys.stderr)  # Outputting text to the error stream (stderr)
    else:
        print(text)  # Write text to standard output (stdout)