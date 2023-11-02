def solution():
    """Salaria is growing oranges this summer. She bought two types of trees. She has 50% of tree A and 50% of tree B. Tree A gives her 10 oranges a month and 60% are good. Tree B gives her 15 oranges and 1/3 are good. If she gets 55 good oranges per month, how many total trees does she have?"""
    # Define the percentage of trees of type A and B
    A_percentage = 0.5
    B_percentage = 0.5

    # Define the number of oranges produced by tree A and the percentage of good oranges
    A_oranges = 10
    A_good_percentage = 0.6

    # Define the number of oranges produced by tree B and the percentage of good oranges
    B_oranges = 15
    B_good_percentage = 1/3

    # Calculate the total number of oranges produced
    total_oranges = 55 / 0.6  # Since 60% are good

    # Calculate the number of trees of type A and B
    A_trees = total_oranges / (A_oranges * A_good_percentage) * A_percentage
    B_trees = total_oranges / (B_oranges * B_good_percentage) * B_percentage

    # Calculate the total number of trees
    total_trees = A_trees + B_trees

    # Return the result
    result = total_trees
    return result

print(solution())