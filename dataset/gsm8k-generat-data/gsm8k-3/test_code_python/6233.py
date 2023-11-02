def solution():
    """There are 50 children at the party. Three-fifths of them are boys. How many of the children are girls?"""
    # Define the total number of children and the fraction that are boys
    total_children = 50
    boys_fraction = 3/5

    # Calculate the number of boys and girls
    boys = total_children * boys_fraction
    girls = total_children - boys

    # Display the number of girls
    result = girls
    return result

print(solution())