import urllib.request


def count_dots_on_i(url: str) -> int:
    mystr = ''
    with urllib.request.urlopen(url) as html:
        mybytes = html.read()
        mystr: str = mybytes.decode("utf8")
        count_i = mystr.count('i')
        return count_i