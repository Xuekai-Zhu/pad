def solution():
    total_seats = 23 * 4  # There are 23 rows of 4 seats in the bus
    passengers_start = 16  # 16 people climb at the start
    passengers_first_stop = passengers_start + 15 - 3  # 15 people board, 3 people get off at the first stop
    passengers_second_stop = passengers_first_stop + 17 - 10  # 17 people board, 10 people get off at the second stop

    # Calculate the number of empty seats after the second stop
    empty_seats = total_seats - passengers_second_stop
    result = empty_seats
    return result

print(solution())