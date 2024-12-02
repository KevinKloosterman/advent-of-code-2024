from utils.funcs import read_file_to_lists_vertical

file_path = 'day01/input.txt'

locids = read_file_to_lists_vertical(file_path, 2)

locids[0].sort()
locids[1].sort()

distances = [abs(locids[0][i] - locids[1][i]) for i in range(len(locids[0]))]

print(sum(distances))
