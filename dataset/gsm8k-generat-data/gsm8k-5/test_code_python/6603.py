def solution():
    seats_per_row = 8  # There are 8 seats in each row
    rows = 12  # There are 12 rows in the airplane

    # Calculate the total number of seats in the airplane
    total_seats = seats_per_row * rows

    # Calculate the number of seats that can be occupied in each row
    occupied_seats_per_row = 3/4 * seats_per_row

    # Calculate the total number of occupied seats in the airplane
    total_occupied_seats = occupied_seats_per_row * rows

    # Calculate the number of seats that will not be occupied
    seats_not_occupied = total_seats - total_occupied_seats
    result = seats_not_occupied
    return result

print(solution())