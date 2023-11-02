def solution():
    """Three times as many children as adults attend a concert on Saturday. An adult ticket costs $7 and a child's ticket costs $3. The theater collected a total of $6,000. How many people bought tickets?"""
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