def solution():
    
    vip_ticket_price = 100
    regular_ticket_price = 50
    num_vip_tickets = 2
    num_regular_tickets = 3
    total_spent = (vip_ticket_price * num_vip_tickets) + (regular_ticket_price * num_regular_tickets)
    remaining_savings = 500 - total_spent
    result = remaining_savings
    return result

print(solution())