def solution():
    """A movie theatre has 250 seats. The cost of a ticket is $6 for an adult and $4 for a child. The theatre is full and contains 188 children. What is the total ticket revenue for this movie session?"""
    # Define the number of seats and the ticket prices
    total_seats = 250
    adult_ticket_price = 6
    child_ticket_price = 4

    # Calculate the number of adult tickets sold
    adult_tickets_sold = total_seats - 188
    # Calculate the revenue from adult tickets
    adult_ticket_revenue = adult_tickets_sold * adult_ticket_price

    # Calculate the revenue from child tickets
    child_ticket_revenue = 188 * child_ticket_price

    # Calculate the total ticket revenue
    total_revenue = adult_ticket_revenue + child_ticket_revenue

    # return the result
    result = total_revenue
    return result

print(solution())