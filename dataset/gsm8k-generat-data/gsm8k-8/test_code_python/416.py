def solution():
    # Define the depth of the river in mid-May
    may_depth = 5

    # Calculate the depth of the river in mid-June
    june_depth = may_depth + 10

    # Calculate the depth of the river in mid-July
    july_depth = 3 * june_depth

    result = july_depth
    return result

print(solution())