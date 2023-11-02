def solution():
    num_children = 3

    # John bought 2 notebooks for each of his children
    john_notebooks = 2 * num_children

    # John's wife bought 5 notebooks for each of their children
    wife_notebooks = 5 * num_children

    # Calculate the total number of notebooks bought
    total_notebooks = john_notebooks + wife_notebooks
    result = total_notebooks
    return result

print(solution())