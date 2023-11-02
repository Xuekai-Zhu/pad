def solution():
    # Calculate the rate at which the drain can empty the pool
    drain_rate = 120 / 4  # The drain empties 120 liters of water in 4 hours

    # Calculate the rate at which the hose can fill the pool
    hose_rate = 120 / 6  # The hose fills 120 liters of water in 6 hours

    # Calculate the net rate of water flow out of the pool
    net_rate = hose_rate - drain_rate  # Water is being added to the pool faster than it is being removed

    # Calculate how much water will be removed from the pool in 3 hours
    water_removed = drain_rate * 3

    # Calculate how much water will be added to the pool in 3 hours
    water_added = hose_rate * 3

    # Calculate the remaining water in the pool after 3 hours
    remaining_water = 120 - water_removed + water_added
    result = remaining_water
    return result

print(solution())