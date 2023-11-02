def solution():
    """John has 3 children. He and his wife are supposed to buy notebooks for their sons but they couldn't agree on how many to buy. So John bought 2 notebooks for each of his children and John's wife bought 5 notebooks for each of them. How many notebooks did they buy in total for their children?"""
    number_of_children = 3
    john_notebooks_per_child = 2
    john_total_notebooks = john_notebooks_per_child * number_of_children
    wife_notebooks_per_child = 5
    wife_total_notebooks = wife_notebooks_per_child * number_of_children
    total_notebooks = john_total_notebooks + wife_total_notebooks
    result = total_notebooks
    return result

print(solution())