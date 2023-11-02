def solution():
    """An opera house has 150 rows; each row has ten seats. The ticket costs $10 per show. 
    How much did the opera house earn from one of the shows if 20% of the seats were not taken?"""
    rows = 150
    seats_per_row = 10
    total_seats = rows * seats_per_row
    seats_taken = total_seats * 0.8
    ticket_price = 10
    revenue = seats_taken * ticket_price
    result = revenue
    return result

print(solution())