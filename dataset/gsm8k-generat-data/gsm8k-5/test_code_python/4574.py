def solution():
    initial_notebooks = 10  # Amanda had 10 notebooks
    ordered_notebooks = 6  # Amanda ordered 6 more notebooks
    lost_notebooks = 2  # Amanda lost 2 notebooks

    # Calculate the total number of notebooks Amanda has now
    total_notebooks = initial_notebooks + ordered_notebooks - lost_notebooks
    result = total_notebooks
    return result

print(solution())