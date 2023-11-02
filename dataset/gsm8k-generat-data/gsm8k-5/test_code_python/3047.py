def solution():
    ticket_cost = 10  # The ticket cost is $10
    total_seats = 20 * 10  # The auditorium has 20 rows and each row has 10 seats
    sold_seats = (3/4) * total_seats  # Only 3/4 of the seats were sold

    # Calculate the total earnings from the play
    total_earnings = sold_seats * ticket_cost
    result = total_earnings
    return result

print(solution())