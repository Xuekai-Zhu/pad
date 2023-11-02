def solution():
    """Eight people fit in a row on an airplane, and there are 12 rows. Only 3/4 of the seats in each row are allowed to be seated. How many seats will not be occupied on that plane?"""
    # Define the number of seats in each row and the proportion allowed to be seated
    SEATS_PER_ROW = 8
    ALLOWED_PROPORTION = 3/4

    # Calculate the number of seats allowed to be seated in each row
    allowed_seats_per_row = round(ALLOWED_PROPORTION * SEATS_PER_ROW)

    # Calculate the total number of seats on the plane
    total_seats = SEATS_PER_ROW * 12

    # Calculate the total number of allowed seats on the plane
    allowed_seats = allowed_seats_per_row * 12

    # Calculate the number of seats that will not be occupied
    vacant_seats = total_seats - allowed_seats

    # Display the number of vacant seats
    result = vacant_seats
    return result

print(solution())