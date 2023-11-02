def solution():
    """A play was held in an auditorium and its ticket costs $10. An auditorium has 20 rows and each row has 10 seats. If only 3/4 of the seats were sold, how much was earned from the play?"""
    ticket_price = 10
    rows = 20
    seats_per_row = 10
    total_seats = rows * seats_per_row
    sold_seats = total_seats * 0.75
    total_earned = sold_seats * ticket_price
    result = total_earned
    return result

print(solution())