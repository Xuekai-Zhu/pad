def solution():
    """John has 3 children. He and his wife are supposed to buy notebooks for their sons but they couldn't agree on how many to buy. So John bought 2 notebooks for each of his children and John's wife bought 5 notebooks for each of them. How many notebooks did they buy in total for their children?"""
    # Define the number of children
    num_children = 3

    # Calculate the number of notebooks John bought
    john_notebooks = num_children * 2

    # Calculate the number of notebooks John's wife bought
    wife_notebooks = num_children * 5

    # Calculate the total number of notebooks
    total_notebooks = john_notebooks + wife_notebooks

    # Display the total number of notebooks
    result = total_notebooks
    return result

print(solution())