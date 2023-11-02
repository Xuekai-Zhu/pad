def solution():
    """Holly wants to plant a wall of privacy trees along her fence line. Her fence is 25 yards long. At maturity, the trees she wants to plant will measure 1.5 feet wide. Right now, these trees are on sale for $8.00 apiece. How much will it cost her to plant a row of the trees to run the length of her fence?"""
    # Define the length of the fence in yards
    fence_length = 25

    # Convert the length to feet
    fence_length_feet = fence_length * 3

    # Define the width of each tree in feet
    tree_width = 1.5

    # Calculate the number of trees needed
    trees_needed = fence_length_feet / tree_width

    # Round up to the nearest whole number
    trees_needed = int(trees_needed) + 1

    # Define the cost per tree
    tree_cost = 8.0

    # Calculate the total cost of purchasing the trees
    total_cost = trees_needed * tree_cost

    # return the result
    result = total_cost
    return result

print(solution())