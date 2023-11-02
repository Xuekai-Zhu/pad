def solution():
    # Calculate total number of seats in the auditorium
    total_seats = 20 * 10

    # Calculate number of seats sold
    seats_sold = int(total_seats * 3/4)

    # Calculate total revenue earned from ticket sales
    revenue = seats_sold * 10
    result = revenue
    return result

print(solution())