def solution():
    """The height of the tree in Kilmer Park is 52 feet. Each year it grows 5 feet. In 8 years, what will the height of the tree be in inches, assuming 1 foot is 12 inches."""
    # Define the initial height of the tree
    TREE_HEIGHT_FEET = 52

    # Define the growth rate of the tree
    GROWTH_RATE_FEET_PER_YEAR = 5

    # Define the number of years
    YEARS = 8

    # Calculate the final height in feet
    final_height_feet = TREE_HEIGHT_FEET + (GROWTH_RATE_FEET_PER_YEAR * YEARS)

    # Convert the height to inches
    final_height_inches = final_height_feet * 12

    # return the result
    result = final_height_inches
    return result

print(solution())