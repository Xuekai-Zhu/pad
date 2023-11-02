def solution():
    # Calculate the number of passengers that fit in 1 bus
    passengers_per_bus = 198 / 9

    # Calculate the number of passengers that fit in 5 buses
    passengers_in_5_buses = passengers_per_bus * 5
    result = passengers_in_5_buses
    return result

print(solution())