def solution():
    # Define the number of seats in the theater and the ticket price
    theater_capacity = 50
    ticket_price = 8

    # Calculate the total revenue for a sold-out show
    sold_out_revenue = theater_capacity * ticket_price

    # Calculate the revenue from the actual number of tickets sold
    actual_revenue = 24 * ticket_price

    # Calculate the amount of money lost due to the unsold seats
    money_lost = sold_out_revenue - actual_revenue
    result = money_lost
    return result

print(solution())