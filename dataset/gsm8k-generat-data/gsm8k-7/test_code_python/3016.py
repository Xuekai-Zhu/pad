def solution():
    length = 10
    width = 8
    depth = 6
    quart_per_volume = 1/120
    cost_per_quart = 3

    # Calculate the volume of the pool
    volume = length * width * depth

    # Calculate the number of quarts of chlorine needed
    num_quarts = volume * quart_per_volume

    # Calculate the total cost of the chlorine
    total_cost = num_quarts * cost_per_quart
    result = total_cost
    return result

print(solution())