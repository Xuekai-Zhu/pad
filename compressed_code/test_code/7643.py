def solution():
    
    base_premium = 50
    accident_increase = 0.1
    ticket_increase = 5
    num_accidents = 1
    num_tickets = 3
    premium_increase = (base_premium * accident_increase * num_accidents) + (num_tickets * ticket_increase)
    new_premium = base_premium + premium_increase
    result = new_premium
    return result

print(solution())