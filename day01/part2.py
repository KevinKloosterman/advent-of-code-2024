from utils.funcs import read_file_to_lists

file_path = 'day01/input.txt'

locids = read_file_to_lists(file_path, 2)

similarity_score = 0

for locid in locids[0]:
    similarity_score += locid * locids[1].count(locid)

print(similarity_score)
