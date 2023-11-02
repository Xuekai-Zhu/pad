def solution():
    total_seats = 500
    seats_taken = (2/5) * total_seats
    broken_seats = (1/10) * total_seats

    # Calculate the number of available seats
    available_seats = total_seats - seats_taken - broken_seats
    result = available_seats
    return result

print(solution())