def solution():
    # Calculate the number of seats currently taken
    taken_seats = 500 * 2/5

    # Calculate the number of broken seats
    broken_seats = 500 * 1/10

    # Calculate the number of available seats
    available_seats = 500 - taken_seats - broken_seats
    result = available_seats
    return result

print(solution())