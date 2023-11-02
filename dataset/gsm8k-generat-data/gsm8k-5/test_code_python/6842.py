def solution():
    total_seats = 500  # The auditorium holds 500 people
    taken_seats = (2/5) * total_seats  # Two-fifths of the seats are currently taken
    broken_seats = total_seats / 10  # 1/10 of the seats are broken

    # Calculate the total number of available seats
    available_seats = total_seats - taken_seats - broken_seats
    result = available_seats
    return result

print(solution())