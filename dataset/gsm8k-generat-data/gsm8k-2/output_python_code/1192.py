def solution():
    """Joe buys 3 oranges, 7 juices, 3 jars of honey, and 4 plants at the market. The fruit costs $4.50 each, the juice was 50 cents each, the jars of honey were $5, and the plants were 2 for $18. How much does Joe spend at the market?"""
    # Calculating total cost of oranges
    orange_cost = 3 * 4.5
    # Calculating total cost of juices
    juice_cost = 7 * 0.5
    # Calculating total cost of honey jars
    honey_cost = 3 * 5
    # Calculating total cost of plants
    plant_cost = 2 * 18
    # Calculating total cost of all items
    total_cost = orange_cost + juice_cost + honey_cost + plant_cost
    result = total_cost
    return result

print(solution())