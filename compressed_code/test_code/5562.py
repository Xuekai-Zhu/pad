def solution():
    
    capacity = 50
    ticket_price = 8.00
    sold_tickets = 24
    unsold_tickets = capacity - sold_tickets
    lost_revenue = unsold_tickets * ticket_price
    result = lost_revenue
    return result

print(solution())