def solution():
    """Two-fifths of the seats in an auditorium that holds 500 people are currently taken. It was found that 1/10 of the seats are broken. How many seats are still available?"""
    total_seats = 500
    taken_seats = total_seats * 2/5
    broken_seats = total_seats * 1/10
    available_seats = total_seats - taken_seats - broken_seats
    result = available_seats
    return result

print(solution())