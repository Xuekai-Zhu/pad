def solution():
    
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