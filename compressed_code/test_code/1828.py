def solution():
    
    base_premium = 50
    accident_increase = 0.1
    ticket_increase = 5
    num_accidents = 1
    num_tickets = 3
    premium = base_premium
    premium += premium * accident_increase * num_accidents
    premium += ticket_increase * num_tickets
    result = premium
    return result

print(solution())