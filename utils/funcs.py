
def read_file_to_lists_vertical(file_path, list_count):
    """
    Reads a file containing space-separated ints vertically into multiple lists.

    Args:
        file_path: Path to the input file.
        list_count: Number of lists to generate based on the file's structure.
    
    Returns:
        A tuple of lists, each containing values from corresponding columns in the file.
    """
    lists = [[] for _ in range(list_count)]

    with open(file_path, 'r') as file:
        for line in file:
            values = line.split()
            
            if len(values) != list_count:
                raise ValueError(f"Each line in the file must contain exactly {list_count} values.")
            
            for i in range(list_count):
                lists[i].append(int(values[i]))
    
    return tuple(lists)

def read_file_to_lists_horizontal(file_path):
    """
    Reads a file containing space-separated ints horizontally into multiple lists.

    Args:
        file_path: Path to the input file.
    
    Returns:
        A list of lists, each containing values from corresponding rows in the file.
    """
    rows = []

    with open(file_path, 'r') as file:
        for line in file:
            row = line.split()
            rows.append([int(i) for i in row])
    
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
