def solution():
    initial_notebooks = 4  # Sara's sister has 4 small notebooks in her closet
    ordered_notebooks = 6  # Sara's sister ordered 6 more notebooks last summer
    lost_notebooks = 2  # Sara's sister lost 2 notebooks

    # Calculate the total number of notebooks Sara's sister has now
    total_notebooks = initial_notebooks + ordered_notebooks - lost_notebooks
    result = total_notebooks
    return result

print(solution())