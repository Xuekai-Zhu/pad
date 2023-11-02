def solution():
    number_of_children = 3  # John has 3 children

    # John buys 2 notebooks for each child
    johns_notebooks = 2 * number_of_children

    # John's wife buys 5 notebooks for each child
    wifes_notebooks = 5 * number_of_children

    # Calculate the total number of notebooks bought
    total_notebooks = johns_notebooks + wifes_notebooks
    result = total_notebooks
    return result

print(solution())