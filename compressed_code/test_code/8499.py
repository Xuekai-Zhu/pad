def solution():
    
    num_tickets = 24
    ticket_cost = 7
    discount_percent = 50
    discount_amount = (num_tickets * ticket_cost) * (discount_percent / 100)
    total_cost = (num_tickets * ticket_cost) - discount_amount
    result = total_cost
    return result

print(solution())