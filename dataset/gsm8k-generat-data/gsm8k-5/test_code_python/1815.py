def solution():
    starting_trees = 2 * 4  # Jim starts with 2 rows of 4 trees each
    added_rows = 15 - 10  # Jim starts adding new rows of trees when he turns 10
    total_rows = 2 + added_rows  # Jim has 2 rows to start and adds one each year

    # Calculate the total number of trees after 5 years of adding rows
    total_trees = starting_trees + (total_rows * 4)

    # Double the number of trees after Jim's 15th birthday
    total_trees *= 2

    result = total_trees
    return result

print(solution())