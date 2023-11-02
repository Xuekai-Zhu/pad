def solution():
    """Salaria is growing oranges this summer. She bought two types of trees. She has 50% of tree A and 50% of tree B. Tree A gives her 10 oranges a month and 60% are good. Tree B gives her 15 oranges and 1/3 are good. If she gets 55 good oranges per month, how many total trees does she have?"""
    total_oranges = 55
    oranges_from_A = 10 * 0.6
    oranges_from_B = 15 * (1/3)
    good_oranges_from_A = total_oranges / 2
    good_oranges_from_B = total_oranges / 2

    # Solve for number of trees
    num_A_trees = (good_oranges_from_A / oranges_from_A) / 0.5
    num_B_trees = (good_oranges_from_B / oranges_from_B) / 0.5
    total_trees = num_A_trees + num_B_trees

    result = total_trees
    return result

print(solution())