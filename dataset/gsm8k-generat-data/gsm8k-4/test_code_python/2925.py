def solution():
    """For the school play, 40 rows of chairs were set up where there were 20 chairs in each row. If only 10 seats were not occupied, how many seats were taken?"""
    # Define the number of rows and chairs per row
    rows = 40
    chairs_per_row = 20

    # Calculate the total number of seats
    total_seats = rows * chairs_per_row

    # Calculate the number of seats occupied
    occupied_seats = total_seats - 10

    # return the result
    result = occupied_seats
    return result

print(solution())