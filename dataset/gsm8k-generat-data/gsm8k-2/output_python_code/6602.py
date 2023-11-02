def solution():
    """Eight people fit in a row on an airplane, and there are 12 rows. Only 3/4 of the seats in each row are allowed to be seated.
    How many seats will not be occupied on that plane?"""
    total_seats = 8 * 12
    allowed_seats_per_row = 8 * 0.75
    total_allowed_seats = allowed_seats_per_row * 12
    unoccupied_seats = total_seats - total_allowed_seats
    result = unoccupied_seats
    return result

print(solution())