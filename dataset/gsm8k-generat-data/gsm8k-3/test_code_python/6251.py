def solution():
    """Susan walked to the market to buy five dozen peaches.  To carry them home, she brought two identically-sized cloth bags and a much smaller knapsack.  Into the knapsack she placed half as many peaches as she placed in each of the two cloth bags. How many peaches did she put in the knapsack?"""
    
    # Find the total number of peaches in dozens
    total_peaches = 5
    
    # Convert total peaches into individual peaches
    total_peaches = total_peaches * 12
    
    # Find the number of peaches that can fit in each cloth bag
    cloth_bag_peaches = total_peaches // 2
    
    # Find the number of peaches that can fit in the knapsack
    knapsack_peaches = cloth_bag_peaches // 2
    
    # Display the number of peaches in the knapsack
    result = knapsack_peaches
    return result

print(solution())