def solution():
    """Joe buys 3 oranges, 7 juices, 3 jars of honey, and 4 plants at the market. The fruit costs $4.50 each, the juice was 50 cents each, the jars of honey were $5, and the plants were 2 for $18. How much does Joe spend at the market?"""
    oranges_cost = 3 * 4.50
    juices_cost = 7 * 0.50
    honey_cost = 3 * 5
    plants_cost = (18/2) * 4
    total_cost = oranges_cost + juices_cost + honey_cost + plants_cost
    result = total_cost
    return result

print(solution())