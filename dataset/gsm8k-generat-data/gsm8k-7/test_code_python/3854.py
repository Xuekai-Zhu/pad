def solution():
    starting_notebooks = 4
    ordered_notebooks = 6
    lost_notebooks = 2

    # Calculate the total number of notebooks Sara's sister has now
    total_notebooks = starting_notebooks + ordered_notebooks - lost_notebooks
    result = total_notebooks
    return result

print(solution())