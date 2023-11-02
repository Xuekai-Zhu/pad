def solution():
    flower_cost = 9
    clay_pot_cost = flower_cost + 20
    soil_bag_cost = flower_cost - 2

    # Calculate the total cost of all items needed to plant the flowers
    total_cost = flower_cost + clay_pot_cost + soil_bag_cost
    result = total_cost
    return result

print(solution())