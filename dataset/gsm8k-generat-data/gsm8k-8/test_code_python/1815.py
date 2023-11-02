def solution():
    # Define the number of trees in Jim's first two rows
    initial_trees = 2 * 4

    # Define the number of years Jim has been planting trees
    planting_years = 15 - 10

    # Define the number of trees Jim has planted in addition to his first two rows
    additional_trees = planting_years * 4

    # Calculate the total number of trees Jim has before doubling them
    total_trees = initial_trees + additional_trees

    # Double the number of trees Jim has on his 15th birthday
    total_trees *= 2

    result = total_trees
    return result

print(solution())