def solution():
    """Chatty prepared three dozen eggs for her four children's Easter activity. Assuming each child gets the same number of eggs, how many eggs does each child receive?"""
    total_eggs = 3 * 12
    num_children = 4
    eggs_per_child = total_eggs // num_children
    result = eggs_per_child
    return result

print(solution())