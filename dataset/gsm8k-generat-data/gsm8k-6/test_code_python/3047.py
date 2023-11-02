def solution():
    # Calculate the total number of seats in the auditorium
    total_seats = 20 * 10  # 20 rows each with 10 seats

    # Calculate the number of seats sold
    seats_sold = (3/4) * total_seats

    # Calculate the total amount earned from sold tickets
    total_earnings = seats_sold * 10  # ticket costs $10

    result = total_earnings
    return result

print(solution())