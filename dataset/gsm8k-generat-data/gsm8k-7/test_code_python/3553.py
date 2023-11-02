def solution():
    # Calculate the rate of the drain and the hose in liters per hour
    drain_rate = 120 / 4
    hose_rate = 120 / 6

    # Calculate the net rate of water being drained and filled in liters per hour
    net_rate = hose_rate - drain_rate

    # Calculate the amount of water left in the pool after 3 hours
    water_left = 120 - (net_rate * 3)
    result = water_left
    return result

print(solution())