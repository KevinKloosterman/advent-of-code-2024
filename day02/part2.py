from utils.funcs import read_file_to_lists_horizontal, check_all_negative_or_positive

def is_safe(rep):
    deltas = [rep[i] - rep[i + 1] for i in range(len(rep) - 1)]
    return (
        check_all_negative_or_positive(deltas) and
        min(deltas) > -4 and 
        max(deltas) < 4 and
        0 not in deltas
    )

file_path = 'day02/input.txt'
reports = read_file_to_lists_horizontal(file_path)

safe_count = 0

for report in reports:
    if is_safe(report):
        safe_count += 1
        continue
    for i in range(len(report)):
        dampened_report = report[:i] + report[i + 1:]
        if is_safe(dampened_report):
            safe_count += 1
            break

print(safe_count)
