from utils.funcs import read_file_to_lists_horizontal

def get_radiants(grid, x_loc, y_loc):
    rows, cols = len(grid), len(grid[0])
    radiants = {
        "upper_left": grid[x_loc - 1][y_loc - 1] if x_loc > 0 and y_loc > 0 else '',
        "upper_right": grid[x_loc - 1][y_loc + 1] if x_loc > 0 and y_loc < cols - 1 else '',
        "bottom_left": grid[x_loc + 1][y_loc - 1] if x_loc < rows - 1 and y_loc > 0 else '',
        "bottom_right": grid[x_loc + 1][y_loc + 1] if x_loc < rows - 1 and y_loc < cols - 1 else '',
    }
    return radiants

def verify_radiants(radiants):
    chars = ['M', 'S']
    upper_left, upper_right, bottom_left, bottom_right = (
        radiants["upper_left"], radiants["upper_right"],
        radiants["bottom_left"], radiants["bottom_right"]
    )
    
    left_right = (
        upper_left in chars and bottom_right in chars and upper_left != bottom_right
    )
    right_left = (
        upper_right in chars and bottom_left in chars and upper_right != bottom_left
    )
    return left_right and right_left

input_path = 'day04/input.txt'

puzzle = read_file_to_lists_horizontal(input_path)

hit_count = 0

for r, row in enumerate(puzzle):
    for c, col in enumerate(row):
        if col == 'A':
            radiants = get_radiants(puzzle, r, c)
            x_mas = verify_radiants(radiants)
            if x_mas:
                hit_count += 1

print(hit_count)
