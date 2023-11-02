def solution():
    """There are 50 children at the party. Three-fifths of them are boys. How many of the children are girls?"""
    # Define the total number of children
    total_children = 50

    # Calculate the number of boys
    boys = total_children * 3 / 5

    # Calculate the number of girls
    girls = total_children - boys

    # Return the result
    result = girls
    return result

print(solution())