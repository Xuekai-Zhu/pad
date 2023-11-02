def solution():
    """For the school play, 40 rows of chairs were set up where there were 20 chairs in each row. If only 10 seats were not occupied, how many seats were taken?"""
    # Define the number of rows and chairs per row
    ROWS = 40
    CHAIRS_PER_ROW = 20

    # Calculate the total number of seats
    total_seats = ROWS * CHAIRS_PER_ROW

    # Calculate the number of seats taken
    seats_taken = total_seats - 10

    # Display the number of seats taken
    result = seats_taken
    return result

print(solution())