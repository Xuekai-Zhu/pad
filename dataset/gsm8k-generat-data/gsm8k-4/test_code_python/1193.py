def solution():
    """Joe buys 3 oranges, 7 juices, 3 jars of honey, and 4 plants at the market. The fruit costs $4.50 each, the juice was 50 cents each, the jars of honey were $5, and the plants were 2 for $18. How much does Joe spend at the market?"""
    # Calculate the cost of the oranges
    orange_cost = 3 * 4.5
    
    # Calculate the cost of the juices
    juice_cost = 7 * 0.5
    
    # Calculate the cost of the honey
    honey_cost = 3 * 5
    
    # Calculate the cost of the plants
    plant_cost = ((4 // 2) * 18) + ((4 % 2) * 9)
    
    # Calculate the total cost
    total_cost = orange_cost + juice_cost + honey_cost + plant_cost
    
    # Return the result
    result = total_cost
    return result

print(solution())