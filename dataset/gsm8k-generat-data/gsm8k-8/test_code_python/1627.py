def solution():
    # Calculate the total amount of water added by the first hose
    first_hose_water = 50 * 3

    # Calculate how much water is left to fill the pool
    remaining_water = pool_capacity - first_hose_water

    # Calculate how much water the second hose can add in 1 hour
    second_hose_water_per_hour = 70

    # Calculate how much water the second hose can add in 2 hours
    second_hose_water = second_hose_water_per_hour * 2

    # Calculate the total amount of water added to the pool
    total_water = first_hose_water + second_hose_water

    result = total_water
    return result

print(solution())