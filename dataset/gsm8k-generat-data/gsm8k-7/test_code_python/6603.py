def solution():
    num_seats_per_row = 8
    num_rows = 12
    allowed_seats_ratio = 0.75

    # Calculate the total number of seats on the plane
    total_seats = num_seats_per_row * num_rows

    # Calculate the number of allowed seats on the plane
    allowed_seats = total_seats * allowed_seats_ratio

    # Calculate the number of seats that will not be occupied
    unoccupied_seats = total_seats - allowed_seats
    result = unoccupied_seats
    return result

print(solution())