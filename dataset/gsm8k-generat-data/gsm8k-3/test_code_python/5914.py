def solution():
    """Salaria is growing oranges this summer. She bought two types of trees. She has 50% of tree A and 50% of tree B.
    Tree A gives her 10 oranges a month and 60% are good. Tree B gives her 15 oranges and 1/3 are good. If she gets 55 good oranges per month, how many total trees does she have?"""
    # Define the number of trees of each type
    trees_a = 0.5  # 50%
    trees_b = 0.5  # 50%

    # Define the number of good oranges from each type of tree
    good_a = 10 * 0.6  # 60% are good
    good_b = 15 * (1 / 3)  # 1/3 are good

    # Define the total number of good oranges
    total_good_oranges = 55

    # Calculate the number of trees of each type needed to produce the total number of good oranges
    trees_a_needed = total_good_oranges / good_a
    trees_b_needed = total_good_oranges / good_b

    # Calculate the total number of trees
    total_trees = trees_a * trees_a_needed + trees_b * trees_b_needed

    # Display the total number of trees
    result = total_trees
    return result

print(solution())