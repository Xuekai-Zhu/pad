def solution():
    """Eight people fit in a row on an airplane, and there are 12 rows. Only 3/4 of the seats in each row are allowed to be seated. How many seats will not be occupied on that plane?"""
    # Define the number of seats per row and the number of rows
    seats_per_row = 8
    num_rows = 12

    # Calculate the total number of seats
    total_seats = seats_per_row * num_rows

    # Calculate the number of seats that are allowed to be seated
    allowed_seats = total_seats * 0.75

    # Calculate the number of seats that will not be occupied
    unoccupied_seats = total_seats - allowed_seats

    # return the result
    result = unoccupied_seats
    return result

print(solution())