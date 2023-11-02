def solution():
    """Bea's mom planted 50 Mahogany and 30 Narra trees on their farm. Due to a typhoon, a total of 5 trees fell. One more Mahogany tree fell than the number of Narra trees that fell. A month after the typhoon, Bea's mom planted twice as much as the number of the Narra and thrice the number of Mahogany trees that fell. How many trees are now on the farm?"""
    # Define the number of Mahogany and Narra trees planted before typhoon
    mahogany_before = 50
    narra_before = 30

    # Calculate the number of trees that fell
    total_fallen = 5
    narra_fallen = (total_fallen - 1) // 2
    mahogany_fallen = total_fallen - narra_fallen

    # Calculate the number of trees planted after the typhoon
    narra_planted = 2 * narra_fallen
    mahogany_planted = 3 * mahogany_fallen

    # Calculate the total number of trees on the farm
    total_trees = mahogany_before + narra_before - total_fallen + narra_planted + mahogany_planted

    # Display the total number of trees
    result = total_trees
    return result

print(solution())