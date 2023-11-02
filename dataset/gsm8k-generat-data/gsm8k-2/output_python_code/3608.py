def solution():
    """A school bus has 4 columns and 10 rows of seats. If the school has 6 buses, how many students can the buses accommodate?"""
    rows = 10
    columns = 4
    seats_per_bus = rows * columns
    total_seats = seats_per_bus * 6
    result = total_seats
    return result

print(solution())