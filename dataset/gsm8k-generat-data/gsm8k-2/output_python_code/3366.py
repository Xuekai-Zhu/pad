def solution():
    """A movie theatre has 250 seats. The cost of a ticket is $6 for an adult and $4 for a child. The theatre is full and contains 188 children. What is the total ticket revenue for this movie session?"""
    adult_ticket_price = 6
    child_ticket_price = 4
    total_seats = 250
    total_children = 188
    total_adults = total_seats - total_children
    adult_revenue = adult_ticket_price * total_adults
    child_revenue = child_ticket_price * total_children
    total_revenue = adult_revenue + child_revenue
    result = total_revenue
    return result

print(solution())