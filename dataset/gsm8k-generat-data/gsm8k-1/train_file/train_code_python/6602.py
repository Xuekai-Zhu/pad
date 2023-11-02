def solution():
    """Eight people fit in a row on an airplane, and there are 12 rows. Only 3/4 of the seats in each row are allowed to be seated. How many seats will not be occupied on that plane?"""
    seats_per_row = 8
    total_rows = 12
    allowed_seats_per_row = int(seats_per_row * 3/4)
    total_allowed_seats = allowed_seats_per_row * total_rows
    total_seats = seats_per_row * total_rows
    seats_not_occupied = total_seats - total_allowed_seats
    result = seats_not_occupied
    return result

print(solution())