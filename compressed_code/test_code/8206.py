def solution():
    
    ticket_cost = 10
    rows = 20
    seats_per_row = 10
    total_seats = rows * seats_per_row
    seats_sold = total_seats * (3/4)
    total_earnings = seats_sold * ticket_cost
    result = total_earnings
    return result

print(solution())