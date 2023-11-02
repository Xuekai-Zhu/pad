def solution():
    """Sara's sister has 4 small notebooks in her closet. Last summer she ordered 6 more notebooks and then lost 2. How many notebooks does Sara's sister have now?"""
    initial_notebooks = 4
    ordered_notebooks = 6
    lost_notebooks = 2
    total_notebooks = initial_notebooks + ordered_notebooks - lost_notebooks
    result = total_notebooks
    return result

print(solution())