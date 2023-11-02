def solution():
    
    jude_tickets = 16
    andrea_tickets = jude_tickets * 2
    sandra_tickets = (jude_tickets / 2) + 4
    total_tickets_sold = jude_tickets + andrea_tickets + sandra_tickets
    tickets_left = 100 - total_tickets_sold
    result = tickets_left
    return result

print(solution())