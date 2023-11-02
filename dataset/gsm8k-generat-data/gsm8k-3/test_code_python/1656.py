def solution():
    """Holly wants to plant a wall of privacy trees along her fence line.  Her fence is 25 yards long.  At maturity, the trees she wants to plant will measure 1.5 feet wide.  Right now, these trees are on sale for $8.00 apiece.  How much will it cost her to plant a row of the trees to run the length of her fence?"""
    # Define constants
    SALE_PRICE = 8  # price per tree on sale
    TREE_WIDTH = 1.5  # width of each tree at maturity in feet
    YARD_TO_FEET = 3  # number of feet in one yard

    # Calculate the number of trees needed
    fence_length = 25  # length of fence in yards
    fence_length_in_feet = fence_length * YARD_TO_FEET  # length of fence in feet
    tree_spacing = TREE_WIDTH  # spacing between trees in feet
    num_trees = int(fence_length_in_feet / tree_spacing)  # round down to nearest integer

    # Calculate the total cost of the trees
    total_cost = num_trees * SALE_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())