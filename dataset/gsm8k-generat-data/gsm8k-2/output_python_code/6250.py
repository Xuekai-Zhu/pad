def solution():
    """Susan walked to the market to buy five dozen peaches. To carry them home, she brought two identically-sized cloth bags and a much smaller knapsack. Into the knapsack she placed half as many peaches as she placed in each of the two cloth bags. How many peaches did she put in the knapsack?"""
    peach_count = 5 * 12
    cloth_bag_count = 2
    knapsack_count = cloth_bag_count / 2
    peach_per_bag = peach_count / cloth_bag_count
    peach_per_knapsack = peach_per_bag / 2
    peach_in_knapsack = knapsack_count * peach_per_knapsack
    result = peach_in_knapsack
    return result

print(solution())