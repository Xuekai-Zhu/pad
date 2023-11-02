def solution():
    num_rows = 23
    num_seats_per_row = 4
    num_initial_passengers = 16
    num_passengers_first_stop = 15
    num_passengers_leaving_first_stop = 3
    num_passengers_second_stop = 17
    num_passengers_leaving_second_stop = 10

    # Calculate the total number of seats on the bus
    total_seats = num_rows * num_seats_per_row

    # Calculate the number of passengers on the bus after the first stop
    num_passengers_after_first_stop = num_initial_passengers + num_passengers_first_stop - num_passengers_leaving_first_stop

    # Calculate the number of passengers on the bus after the second stop
    num_passengers_after_second_stop = num_passengers_after_first_stop + num_passengers_second_stop - num_passengers_leaving_second_stop

    # Calculate the number of empty seats on the bus after the second stop
    num_empty_seats = total_seats - num_passengers_after_second_stop
    result = num_empty_seats
    return result

print(solution())