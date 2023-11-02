def solution():
    """A play was held in an auditorium and its ticket costs $10. An auditorium has 20 rows and each row has 10 seats.
    If only 3/4 of the seats were sold, how much was earned from the play?"""
    ticket_cost = 10
    rows = 20
    seats_per_row = 10
    total_seats = rows * seats_per_row
    seats_sold = total_seats * (3/4)
    total_earnings = seats_sold * ticket_cost
    result = total_earnings
    return result

print(solution())