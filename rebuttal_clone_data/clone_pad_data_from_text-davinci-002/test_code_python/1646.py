def solution():
    passengers_per_bus = 198
    buses = 9
    desired_buses = 5
    passengers = passengers_per_bus * buses
    result = passengers / desired_buses
    return result

print(solution())