import re
from utils.funcs import read_file_to_string

def mul(a, b):
    return a * b

my_string = read_file_to_string('day03/input.txt', linebreaks=False)

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
matches = [match.group() for match in re.finditer(pattern, my_string)]

print(matches)

result = 0

do = True
for match in matches:
    if match == "do()":
        do = True
    elif match == "don't()":
        do = False
    else:
        if do:
            result += eval(match)

print(result)
