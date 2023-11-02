def solution():
    """A concert ticket costs $40. Mr. Benson bought 12 tickets and received a 5% discount for every ticket bought that exceeds 10. How much did Mr. Benson pay in all?"""
    # Define the ticket price and the number of tickets bought
    ticket_price = 40
    tickets_bought = 12

    # Calculate the discount amount for each extra ticket above 10
    extra_ticket_discount = ticket_price * 0.05

    # Calculate the total cost before any discounts
    total_cost = ticket_price * tickets_bought

    # Apply the discount for extra tickets above 10
    if tickets_bought > 10:
        extra_tickets = tickets_bought - 10
        extra_discount = extra_tickets * extra_ticket_discount
        total_cost -= extra_discount

    # Return the final cost after any discounts
    result = total_cost
    return result

print(solution())