def solution():
    # Calculate the rate of draining and filling
    drain_rate = 120 / 4  # liters per hour
    fill_rate = 120 / 6  # liters per hour

    # Calculate the net rate of water loss
    net_rate = fill_rate - drain_rate  # liters per hour

    # Calculate the amount of water left after 3 hours
    water_left = 120 - (net_rate * 3)

    result = water_left
    return result

print(solution())