def solution():
    base_premium = 50
    accident_increase = 10
    ticket_increase = 5
    num_accidents = 1
    num_tickets = 3
    total_increase = (accident_increase * num_accidents) + (ticket_increase * num_tickets)
    new_premium = base_premium + total_increase
    result = new_premium
    return result

print(solution())