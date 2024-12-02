from utils.funcs import read_file_to_lists_horizontal, check_all_negative_or_positive

file_path = 'day02/input.txt'

reports = read_file_to_lists_horizontal(file_path)

safe_count = 0

for report in reports:
    deltas = []
    for i in range(len(report) - 1):
        deltas.append(report[i] - report[i + 1])
    if check_all_negative_or_positive(deltas):
        if min(deltas) > -4 and max(deltas) < 4:
            if 0 not in deltas:
                safe_count += 1

print(safe_count)
