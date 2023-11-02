def solution():
    max_capacity = 50
    ticket_price = 8.0
    num_tickets_sold = 24

    # Calculate the revenue they would have earned if they sold out
    max_revenue = max_capacity * ticket_price

    # Calculate the revenue they actually earned
    actual_revenue = num_tickets_sold * ticket_price

    # Calculate the amount of money they lost
    lost_revenue = max_revenue - actual_revenue
    result = lost_revenue
    return result

print(solution())