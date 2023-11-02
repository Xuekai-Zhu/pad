def solution():
    """Jim has 2 rows of 4 trees to start. When he turns 10 he decides to plant a new row of trees every year on his birthday. On his 15th birthday after he doubles the number of trees he has. How many trees does he have?"""
    # Define the initial number of rows and trees per row
    initial_rows = 2
    trees_per_row = 4

    # Initialize the number of trees to the initial number of rows and trees per row
    num_trees = initial_rows * trees_per_row

    # Determine how many years Jim has been planting trees
    years_planting = 15 - 10

    # Add one row of trees for each year Jim has been planting
    num_trees += years_planting * trees_per_row

    # Double the number of trees on Jim's 15th birthday
    if years_planting >= 5:
        num_trees *= 2

    # Display the total number of trees Jim has
    result = num_trees
    return result

print(solution())