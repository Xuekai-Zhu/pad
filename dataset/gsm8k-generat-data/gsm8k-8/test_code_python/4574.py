def solution():
    start_notebooks = 10
    ordered_notebooks = 6
    lost_notebooks = 2

    total_notebooks = start_notebooks + ordered_notebooks - lost_notebooks

    result = total_notebooks
    return result

print(solution())