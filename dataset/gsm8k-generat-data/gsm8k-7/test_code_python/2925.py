def solution():
    num_rows = 40
    num_chairs_per_row = 20
    num_unoccupied_seats = 10

    # Calculate the total number of seats available
    total_num_seats = num_rows * num_chairs_per_row

    # Calculate the number of seats that were taken
    num_seats_taken = total_num_seats - num_unoccupied_seats
    result = num_seats_taken
    return result

print(solution())