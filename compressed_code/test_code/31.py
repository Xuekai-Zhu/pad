def solution():
    
    ticket_price = 40
    num_tickets = 12
    discount = 0.05
    if num_tickets > 10:
        extra_tickets = num_tickets - 10
        extra_cost = extra_tickets * ticket_price * (1 - discount)
        total_cost = (10 * ticket_price) + extra_cost
    else:
        total_cost = num_tickets * ticket_price
    result = total_cost
    return result

print(solution())