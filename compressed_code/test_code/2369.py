def solution():
    
    ticket_price = 10
    rows = 20
    seats_per_row = 10
    total_seats = rows * seats_per_row
    sold_seats = total_seats * 0.75
    total_earned = sold_seats * ticket_price
    result = total_earned
    return result

print(solution())