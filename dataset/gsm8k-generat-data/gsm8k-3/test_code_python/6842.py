def solution():
    """Two-fifths of the seats in an auditorium that holds 500 people are currently taken. It was found that 1/10 of the seats are broken. How many seats are still available?"""
    # Define the total number of seats in the auditorium
    TOTAL_SEATS = 500

    # Calculate the number of seats that are currently taken
    taken_seats = (2/5) * TOTAL_SEATS

    # Calculate the number of seats that are broken
    broken_seats = TOTAL_SEATS * (1/10)

    # Calculate the number of seats that are still available
    available_seats = TOTAL_SEATS - taken_seats - broken_seats

    # Display the number of available seats
    result = available_seats
    return result

print(solution())