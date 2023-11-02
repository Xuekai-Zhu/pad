def solution():
    
    adult_ticket_price = 7
    child_ticket_price = 3
    total_tickets = 0
    
    for adults in range(1, 2000):
        children = 3 * adults
        revenue = adults * adult_ticket_price + children * child_ticket_price
        if revenue == 6000:
            total_tickets = adults + children
            break
    
    result = total_tickets
    return result

print(solution())