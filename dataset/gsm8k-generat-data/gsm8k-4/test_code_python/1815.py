def solution():
    """Jim has 2 rows of 4 trees to start. When he turns 10 he decides to plant a new row of trees every year on his birthday. On his 15th birthday after he doubles the number of trees he has. How many trees does he have?"""
    # Define the initial number of rows and trees per row
    rows = 2
    trees_per_row = 4

    # Calculate the age at which Jim doubles the number of trees he has
    doubling_age = 15

    # Plant a new row of trees every year until Jim's doubling age
    for age in range(10, doubling_age):
        rows += 1
        trees_per_row += 1

    # Calculate the total number of trees Jim has at his doubling age
    total_trees = (rows * trees_per_row) * 2

    # Return the result
    result = total_trees
    return result

print(solution())