def solution():
    """
    Vincent can buy flowers in packages of 3 for $2.50 or in packages of 2 for $1. 
    How much money does he save by buying 18 flowers at the better price?
    """
    cost_3_for_2 = 2.5
    cost_2_for_1 = 1
    flowers = 18
    
    # Calculate cost if buying in packages of 3
    packages_of_3 = flowers // 3
    cost_3 = packages_of_3 * cost_3_for_2
    
    # Calculate cost if buying in packages of 2
    remaining_flowers = flowers % 3
    packages_of_2 = remaining_flowers // 2
    cost_2 = packages_of_2 * cost_2_for_1
    
    # Calculate total cost and savings
    total_cost = cost_3 + cost_2
    savings = (flowers * cost_2_for_1) - total_cost
    
    return savings

print(solution())