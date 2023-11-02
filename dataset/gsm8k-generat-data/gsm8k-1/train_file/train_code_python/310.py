def solution():
    """The seats of a bus are arranged in 23 rows of 4 seats. At the start, 16 people climb. At the first stop, 15 people board the bus and 3 get off. At the second stop, 17 people get on the bus and 10 get off. How many empty seats are there after the second stop?"""
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