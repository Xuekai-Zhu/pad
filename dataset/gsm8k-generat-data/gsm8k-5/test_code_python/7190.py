def solution():
    capacity = 50  # The movie theater can hold 50 people at a time
    ticket_price = 8.00  # The ticket price is $8.00
    sold_tickets = 24  # They only sold 24 tickets on a Tuesday night

    # Calculate the revenue they would have earned if they sold out
    max_revenue = capacity * ticket_price

    # Calculate the actual revenue they earned
    actual_revenue = sold_tickets * ticket_price

    # Calculate the amount of money they lost by not selling out
    lost_revenue = max_revenue - actual_revenue
    result = lost_revenue
    return result

print(solution())