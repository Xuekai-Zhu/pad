def solution():
    """A concert ticket costs $40. Mr. Benson bought 12 tickets and received a 5% discount for every ticket bought that exceeds 10. How much did Mr. Benson pay in all?"""
    # Define the ticket price and the number of tickets bought
    ticket_price = 40
    num_tickets = 12

    # Calculate the total cost before and after discount
    cost_before_discount = ticket_price * num_tickets
    cost_after_discount = cost_before_discount

    # Apply the discount if applicable
    if num_tickets > 10:
        discount = (num_tickets - 10) * 0.05 * ticket_price
        cost_after_discount = cost_before_discount - discount

    # Return the final cost
    result = cost_after_discount
    return result

print(solution())