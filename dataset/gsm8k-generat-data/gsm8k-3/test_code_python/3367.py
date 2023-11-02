def solution():
    """A movie theatre has 250 seats. The cost of a ticket is $6 for an adult and $4 for a child. The theatre is full and contains 188 children. What is the total ticket revenue for this movie session?"""
    # Set the number of seats and ticket prices
    TOTAL_SEATS = 250
    ADULT_TICKET_PRICE = 6
    CHILD_TICKET_PRICE = 4

    # Calculate the number of adult tickets sold
    adult_tickets = TOTAL_SEATS - 188

    # Calculate the revenue from adult tickets
    adult_revenue = adult_tickets * ADULT_TICKET_PRICE

    # Calculate the revenue from child tickets
    child_revenue = 188 * CHILD_TICKET_PRICE

    # Calculate the total revenue
    total_revenue = adult_revenue + child_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())