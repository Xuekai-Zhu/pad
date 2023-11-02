def solution():
    
    vip_tickets = 2
    regular_tickets = 3
    vip_ticket_price = 100
    regular_ticket_price = 50
    total_cost = (vip_tickets * vip_ticket_price) + (regular_tickets * regular_ticket_price)
    savings_left = 500 - total_cost
    result = savings_left
    return result

print(solution())