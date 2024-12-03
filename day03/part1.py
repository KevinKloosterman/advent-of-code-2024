import re
from utils.funcs import read_file_to_string

my_string = read_file_to_string('day03/input.txt', linebreaks=False)

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
mul_funcs = re.findall(pattern, my_string)

result = 0

for mul_func in mul_funcs:
    result += int(mul_func[0]) * int(mul_func[1])

print(result)
