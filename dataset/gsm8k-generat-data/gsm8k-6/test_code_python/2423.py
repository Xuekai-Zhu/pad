def solution():
    # Calculate how much water is added to the tank during the rainstorm
    added_water = 2 * 90  # water flows into the tank at a rate of 2 L/min for 90 minutes

    # Add the added water to the initial amount of water in the tank
    total_water = 100 + added_water
    result = total_water
    return result

print(solution())