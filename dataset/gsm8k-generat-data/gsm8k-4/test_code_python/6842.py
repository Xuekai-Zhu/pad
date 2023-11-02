def solution():
    """Two-fifths of the seats in an auditorium that holds 500 people are currently taken. It was found that 1/10 of the seats are broken. How many seats are still available?"""
    # Define the total number of seats
    total_seats = 500

    # Calculate the number of seats currently taken
    taken_seats = total_seats * 2/5

    # Calculate the number of broken seats
    broken_seats = total_seats * 1/10

    # Calculate the number of available seats
    available_seats = total_seats - taken_seats - broken_seats

    # Return the result
    result = available_seats
    return result

print(solution())