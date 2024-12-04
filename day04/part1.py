from utils.funcs import read_file_to_lists_horizontal, read_file_to_lists_vertical

def count_hits(grid):
    hit_count = 0
    for row in grid:
        xmas_count = row.count('XMAS')
        samx_count = row.count('SAMX')
        hit_count += xmas_count + samx_count
    return hit_count

def skew_right(grid):
    row_count = len(grid)
    col_count = len(grid[0])

    skewed = ['' for _ in range(row_count + col_count - 1)]
    for row in range(row_count):
        for col in range(col_count):
            diagonal_index = row + col
            skewed[diagonal_index] += grid[row][col]
    
    return skewed

def skew_left(grid):
    row_count = len(grid)
    col_count = len(grid[0])

    skewed = ['' for _ in range(row_count + col_count - 1)]

    for row in range(row_count):
        for col in range(col_count):
            diagonal_index = (col_count - 1 - col) + row
            skewed[diagonal_index] += grid[row][col]

    return skewed

input_path = 'day04/input.txt'

hits = 0

puzzle_hori = read_file_to_lists_horizontal(input_path)
horizontal_hits = count_hits(puzzle_hori)
hits += horizontal_hits

puzzle_vert = read_file_to_lists_vertical(input_path)
vertical_hits = count_hits(puzzle_vert)
hits += vertical_hits

puzzle_skew_r = skew_right(puzzle_hori)
skew_r_hits = count_hits(puzzle_skew_r)
hits += skew_r_hits

puzzle_skew_l = skew_left(puzzle_hori)
skew_l_hits = count_hits(puzzle_skew_l)
hits += skew_l_hits

print(hits)
