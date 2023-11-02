def solution():
    """John has a large water collection tank.  The tank can hold 200 gallons.  It weighs 80 pounds empty.  A rainstorm fills it to 80% of capacity.  If a gallon of water weighs 8 pounds, how much does it weigh now?"""
    # Define the capacity of the tank and the weight of an empty tank
    CAPACITY = 200 # gallons
    EMPTY_WEIGHT = 80 # pounds

    # Calculate the number of gallons filled during the rainstorm
    filled_gallons = 0.8 * CAPACITY

    # Calculate the weight of the water in the tank
    water_weight = filled_gallons * 8 # 1 gallon of water weighs 8 pounds

    # Calculate the total weight of the tank and water
    total_weight = EMPTY_WEIGHT + water_weight

    # Display the total weight
    result = total_weight
    return result

print(solution())