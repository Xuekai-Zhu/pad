def solution():
    """A movie theater can hold 50 people at a time. They charge $8.00 a ticket. On a Tuesday night they only sold 24 tickets. By not selling out, how much money did they lose?"""
    capacity = 50
    ticket_price = 8.00
    sold_tickets = 24
    unsold_tickets = capacity - sold_tickets
    lost_revenue = unsold_tickets * ticket_price
    result = lost_revenue
    return result

print(solution())