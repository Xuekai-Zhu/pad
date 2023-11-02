def solution():
    # Calculate the total distance Carla needs to travel
    total_distance = 8 + 6 + 12 + 2*(6 + 12)

    # Calculate the amount of gas Carla will need based on her car's MPG
    gas_needed = total_distance / 25

    # Calculate the cost of the gas
    gas_cost = gas_needed * 2.50

    result = gas_cost
    return result

print(solution())