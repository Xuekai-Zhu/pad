def solution():
    ticket_cost = 10
    num_rows = 20
    num_seats_per_row = 10
    sold_percentage = 0.75  # 3/4 of seats were sold

    # Calculate the total number of seats in the auditorium
    total_seats = num_rows * num_seats_per_row

    # Calculate the number of seats sold
    seats_sold = total_seats * sold_percentage

    # Calculate the total amount earned from ticket sales
    total_earnings = seats_sold * ticket_cost
    result = total_earnings
    return result

print(solution())