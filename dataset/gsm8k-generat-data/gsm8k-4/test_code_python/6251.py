def solution():
    """Susan walked to the market to buy five dozen peaches. To carry them home, she brought two identically-sized cloth bags and a much smaller knapsack. Into the knapsack she placed half as many peaches as she placed in each of the two cloth bags. How many peaches did she put in the knapsack?"""
    # Define the number of peaches in one dozen
    PEACHES_PER_DOZEN = 12

    # Define the total number of peaches
    total_peaches = 5 * PEACHES_PER_DOZEN

    # Define the number of peaches in each cloth bag
    peaches_per_bag = total_peaches / 2

    # Define the number of peaches in the knapsack
    knapsack_peaches = peaches_per_bag / 2

    result = knapsack_peaches
    return result

print(solution())