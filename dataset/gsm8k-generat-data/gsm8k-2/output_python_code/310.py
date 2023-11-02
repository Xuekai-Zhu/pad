def solution():
    """The seats of a bus are arranged in 23 rows of 4 seats. At the start, 16 people climb. At the first stop, 15 people board the bus and 3 get off. At the second stop, 17 people get on the bus and 10 get off. How many empty seats are there after the second stop?"""
    rows = 23
    seats_per_row = 4
    total_seats = rows * seats_per_row
    passengers_start = 16
    passengers_first_stop = passengers_start + 15 - 3
    passengers_second_stop = passengers_first_stop + 17 - 10
    empty_seats = total_seats - passengers_second_stop
    result = empty_seats
    return result

print(solution())