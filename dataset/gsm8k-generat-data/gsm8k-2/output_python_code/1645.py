def solution():
    """198 passengers fit into 9 buses. How many passengers fit in 5 buses?"""
    passengers_per_bus = 198 / 9
    passengers_in_5_buses = passengers_per_bus * 5
    result = passengers_in_5_buses
    return result

print(solution())