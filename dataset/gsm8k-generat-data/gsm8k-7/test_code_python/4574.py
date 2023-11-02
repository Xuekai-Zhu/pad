def solution():
    current_num_notebooks = 10
    num_notebooks_ordered = 6
    num_notebooks_lost = 2

    # Calculate the new number of notebooks Amanda has
    new_num_notebooks = current_num_notebooks + num_notebooks_ordered - num_notebooks_lost
    result = new_num_notebooks
    return result

print(solution())