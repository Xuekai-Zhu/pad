def solution():
    """John has 3 children. He and his wife are supposed to buy notebooks for their sons but they couldn't agree on how many to buy. So John bought 2 notebooks for each of his children and John's wife bought 5 notebooks for each of them. How many notebooks did they buy in total for their children?"""
    children = 3
    john_notebooks_per_child = 2
    wife_notebooks_per_child = 5
    john_total_notebooks = children * john_notebooks_per_child
    wife_total_notebooks = children * wife_notebooks_per_child
    total_notebooks = john_total_notebooks + wife_total_notebooks
    result = total_notebooks
    return result

print(solution())