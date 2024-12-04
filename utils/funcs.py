
def read_file_to_lists_vertical(file_path):
    """
    Reads a file containing space-separated ints vertically into multiple lists (by columns).

    Args:
        file_path: Path to the input file.
    
    Returns:
        A list of lists, each containing values from corresponding columns in the file.
    """
    with open(file_path, 'r') as file:
        rows = [list(line.strip()) for line in file]
    
    columns = list(zip(*rows))
    
    concatenated_columns = [''.join(col) for col in columns]
    
    return concatenated_columns

def read_file_to_lists_horizontal(file_path):
    """
    Reads a file containing space-separated ints horizontally into multiple lists.

    Args:
        file_path: Path to the input file.
    
    Returns:
        A list of lists, each containing values from corresponding rows in the file.
    """
    with open(file_path, 'r') as file:
        rows = [line.strip() for line in file]
    
    return rows

def read_file_to_string(file_path, linebreaks):
    """
    Reads a .txt file into a single string.

    Args:
        file_path (str): Path to the input file.
        linebreaks (bool): Whether to include linebreaks or return single line.
    
    Returns:
        str: the full content of the file
    """
    my_string = ""

    with open(file_path, 'r') as file:
        for line in file:
            if linebreaks:
                my_string += line
            else:
                my_string += line[:-1]
    
    return my_string

def check_all_negative_or_positive(lst):
    return len(set(x > 0 for x in lst)) == 1
