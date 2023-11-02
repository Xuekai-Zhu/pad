def solution():
    """Susan walked to the market to buy five dozen peaches. To carry them home, she brought two identically-sized cloth bags and a much smaller knapsack. Into the knapsack she placed half as many peaches as she placed in each of the two cloth bags. How many peaches did she put in the knapsack?"""
    total_peaches = 5 * 12
    cloth_bags = 2
    knapsack_peaches = (total_peaches - (total_peaches // 2)) // cloth_bags
    result = knapsack_peaches
    return result

print(solution())