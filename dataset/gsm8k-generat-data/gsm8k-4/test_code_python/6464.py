def solution():
    """Bea's mom planted 50 Mahogany and 30 Narra trees on their farm. Due to a typhoon, a total of 5 trees fell. One more Mahogany tree fell than the number of Narra trees that fell. A month after the typhoon, Bea's mom planted twice as much as the number of the Narra and thrice the number of Mahogany trees that fell. How many trees are now on the farm?"""
    # Define the initial number of Mahogany and Narra trees
    mahogany_trees = 50
    narra_trees = 30

    # Define the number of fallen trees
    fallen_trees = 5
    narra_fallen = (fallen_trees - 1) / 2
    mahogany_fallen = fallen_trees - narra_fallen

    # Calculate the number of trees planted after the typhoon
    narra_planted = narra_fallen * 2
    mahogany_planted = mahogany_fallen * 3

    # Calculate the total number of trees after the typhoon and planting
    total_trees = mahogany_trees + narra_trees - fallen_trees + narra_planted + mahogany_planted

    # return the result
    result = total_trees
    return result

print(solution())