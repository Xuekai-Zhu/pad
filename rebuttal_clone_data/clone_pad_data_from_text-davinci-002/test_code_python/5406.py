def solution():
    adult_ticket = 6
    child_ticket = adult_ticket - 6
    total_cost = 77
    total_tickets = 5
    cost_of_adult_ticket = (total_cost - (total_tickets * child_ticket)) / total_tickets
    result = cost_of_adult_ticket
    
    return result

print(solution())