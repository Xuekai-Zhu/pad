def solution():
    # Calculate the total number of seats on the plane
    total_seats = 8 * 12

    # Calculate the number of seats that are not allowed to be seated in each row
    unallowed_seats_per_row = 0.25 * 8

    # Calculate the total number of unallowed seats on the plane
    total_unallowed_seats = unallowed_seats_per_row * 12

    # Calculate the number of seats that will not be occupied
    unoccupied_seats = total_unallowed_seats

    result = unoccupied_seats
    return result

print(solution())