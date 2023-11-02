def solution():
    """Amanda had 10 notebooks. This week, she ordered 6 more and then lost 2. How many notebooks does Amanda have now?"""
    starting_notebooks = 10
    ordered_notebooks = 6
    lost_notebooks = 2
    total_notebooks = starting_notebooks + ordered_notebooks - lost_notebooks
    result = total_notebooks
    return result

print(solution())