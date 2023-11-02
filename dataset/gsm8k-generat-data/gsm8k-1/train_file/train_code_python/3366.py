def solution():
    """A movie theatre has 250 seats. The cost of a ticket is $6 for an adult and $4 for a child. The theatre is full and contains 188 children. What is the total ticket revenue for this movie session?"""
    total_seats = 250
    adult_ticket_price = 6
    child_ticket_price = 4
    adult_tickets_sold = total_seats - 188
    child_tickets_sold = 188
    adult_ticket_revenue = adult_tickets_sold * adult_ticket_price
    child_ticket_revenue = child_tickets_sold * child_ticket_price
    total_revenue = adult_ticket_revenue + child_ticket_revenue
    result = total_revenue
    return result

print(solution())