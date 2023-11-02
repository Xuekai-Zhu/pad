def solution():
    """An opera house has 150 rows; each row has ten seats. The ticket costs $10 per show. How much did the opera house earn from one of the shows if 20% of the seats were not taken?"""
    total_seats = 150 * 10
    seats_taken = int(total_seats * 0.8)
    ticket_price = 10
    total_earnings = seats_taken * ticket_price
    result = total_earnings
    return result

print(solution())