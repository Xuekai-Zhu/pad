def solution():
    tank_capacity = 200  # The tank capacity is 200 gallons
    tank_empty_weight = 80  # The weight of the empty tank is 80 pounds
    filled_capacity = tank_capacity * 0.8  # The tank is filled to 80% of capacity
    water_weight = filled_capacity * 8  # The weight of the water in the tank
    total_weight = tank_empty_weight + water_weight  # The total weight of the tank and water

    result = total_weight
    return result

print(solution())