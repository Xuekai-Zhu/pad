def solution():
    """John has a large water collection tank. The tank can hold 200 gallons. It weighs 80 pounds empty. A rainstorm fills it to 80% of capacity. If a gallon of water weighs 8 pounds, how much does it weigh now?"""
    # Define the capacity of the tank and its weight when empty
    tank_capacity = 200
    empty_weight = 80

    # Calculate the volume of water in the tank after the rainstorm
    water_volume = tank_capacity * 0.8

    # Calculate the weight of the water in the tank
    water_weight = water_volume * 8

    # Calculate the total weight of the tank and the water
    total_weight = empty_weight + water_weight

    result = total_weight
    return result

print(solution())