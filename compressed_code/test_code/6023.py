def solution():
    
    rows = 23
    seats_per_row = 4
    initial_passengers = 16
    first_stop_board = 15
    first_stop_off = 3
    second_stop_board = 17
    second_stop_off = 10
    total_seats = rows * seats_per_row
    current_passengers = initial_passengers + first_stop_board - first_stop_off + second_stop_board - second_stop_off
    empty_seats = total_seats - current_passengers
    result = empty_seats
    return result

print(solution())