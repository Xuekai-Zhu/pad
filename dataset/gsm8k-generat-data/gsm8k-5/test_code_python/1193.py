def solution():
    # Calculate the cost of the oranges
    cost_oranges = 3 * 4.50  # 3 oranges at $4.50 each

    # Calculate the cost of the juices
    cost_juices = 7 * 0.50  # 7 juices at 50 cents each

    # Calculate the cost of the jars of honey
    cost_honey = 3 * 5  # 3 jars of honey at $5 each

    # Calculate the cost of the plants
    cost_plants = (4 // 2) * 18  # 4 plants, with 2 costing $18

    # Calculate the total cost of all items
    total_cost = cost_oranges + cost_juices + cost_honey + cost_plants
    result = total_cost
    return result

print(solution())