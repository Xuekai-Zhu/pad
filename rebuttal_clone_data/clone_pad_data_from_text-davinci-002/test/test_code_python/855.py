def solution():
    theater_capacity = 400
    percent_filled = 80
    seats_filled = theater_capacity * (percent_filled / 100)
    ticket_price = 30
    total_tickets_sold = seats_filled * 3
    total_revenue = total_tickets_sold * ticket_price
    result = total_revenue
    return result

print(solution())