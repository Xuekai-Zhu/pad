def solution():
    """A small theater company sells tickets to a show. They have a 400 seat theater and fill to 80% capacity. Each ticket cost $30. They repeated the same performance 2 other days. How much did they make?"""
    total_seats = 400
    capacity_percentage = 0.8
    filled_seats = total_seats * capacity_percentage
    ticket_price = 30
    total_revenue = filled_seats * ticket_price * 3
    result = total_revenue
    return result

print(solution())