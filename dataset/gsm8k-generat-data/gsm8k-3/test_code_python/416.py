def solution():
    """In mid-May, the river flowing through Moreland is five feet deep. By mid-June, the river is 10 feet deeper than mid-May. By mid-July, the river is three times deeper than mid-June. How many feet deep is the river by mid-July?"""
    # Define the depth of the river in mid-May
    may_depth = 5

    # Calculate the depth of the river in mid-June
    june_depth = may_depth + 10

    # Calculate the depth of the river in mid-July
    july_depth = 3 * june_depth

    # Display the depth of the river in mid-July
    result = july_depth
    return result

print(solution())