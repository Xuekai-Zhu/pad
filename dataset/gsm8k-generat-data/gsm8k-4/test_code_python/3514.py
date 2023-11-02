def solution():
    """John has 3 children. He and his wife are supposed to buy notebooks for their sons but they couldn't agree on how many to buy. So John bought 2 notebooks for each of his children and John's wife bought 5 notebooks for each of them. How many notebooks did they buy in total for their children?"""
    # Define the number of children and the number of notebooks each parent bought
    num_children = 3
    john_notebooks = 2
    wife_notebooks = 5

    # Calculate the total number of notebooks bought by both parents
    total_notebooks = (john_notebooks * num_children) + (wife_notebooks * num_children)

    # return the result
    result = total_notebooks
    return result

print(solution())