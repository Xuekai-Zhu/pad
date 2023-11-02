def solution():
    
    theater_capacity = 400
    percent_filled = 0.8
    seats_filled = theater_capacity * percent_filled
    ticket_price = 30
    total_revenue = seats_filled * ticket_price * 3
    result = total_revenue
    return result

print(solution())