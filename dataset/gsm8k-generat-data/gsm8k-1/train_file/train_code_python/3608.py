def solution():
    """A school bus has 4 columns and 10 rows of seats. If the school has 6 buses, how many students can the buses accommodate?"""
    seats_per_bus = 4 * 10
    num_buses = 6
    total_seats = seats_per_bus * num_buses
    result = total_seats
    return result

print(solution())