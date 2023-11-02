def solution():
    # Calculate the average number of passengers per bus
    avg_passengers_per_bus = 198 / 9

    # Calculate the number of passengers that can fit in 5 buses
    passengers_in_5_buses = avg_passengers_per_bus * 5
    result = passengers_in_5_buses
    return result

print(solution())