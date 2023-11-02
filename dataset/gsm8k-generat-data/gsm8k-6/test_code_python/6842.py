def solution():
    # Calculate the number of seats currently taken
    seats_taken = (2/5) * 500

    # Calculate the number of broken seats
    broken_seats = (1/10) * 500

    # Calculate the number of seats still available
    seats_available = 500 - seats_taken - broken_seats
    
    result = seats_available
    return result

print(solution())