def solution():
    """A movie theater can hold 50 people at a time. They charge $8.00 a ticket. On a Tuesday night they only sold 24 tickets. By not selling out, how much money did they lose?"""
    max_capacity = 50
    ticket_price = 8.00
    tickets_sold = 24
    unsold_tickets = max_capacity - tickets_sold
    potential_earnings = unsold_tickets * ticket_price
    result = potential_earnings
    return result

print(solution())