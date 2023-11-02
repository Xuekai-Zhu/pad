def solution():
    
    adult_ticket_cost = 8
    child_ticket_cost = 3
    total_money = 35
    max_children = (total_money - adult_ticket_cost) // child_ticket_cost
    result = max_children
    return result

print(solution())