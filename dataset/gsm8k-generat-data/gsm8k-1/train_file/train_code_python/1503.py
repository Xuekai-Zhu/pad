def solution():
    """A small theater company sells tickets to a show. They have a 400 seat theater and fill to 80% capacity. Each ticket cost $30. They repeated the same performance 2 other days. How much did they make?"""
    theater_capacity = 400
    percent_filled = 0.8
    seats_filled = theater_capacity * percent_filled
    ticket_price = 30
    total_revenue = seats_filled * ticket_price * 3
    result = total_revenue
    return result

print(solution())