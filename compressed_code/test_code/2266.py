def solution():
    
    jude_tickets = 16
    andrea_tickets = 2 * jude_tickets
    sandra_tickets = 4 + (0.5 * jude_tickets)
    total_tickets = jude_tickets + andrea_tickets + sandra_tickets
    remaining_tickets = 100 - total_tickets
    result = remaining_tickets
    return result

print(solution())