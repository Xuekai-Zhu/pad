def solution():
    
    num_adults = 5
    num_children = 2
    concession_cost = 12
    child_ticket_cost = 7
    total_cost = 76
    adult_ticket_cost = (total_cost - concession_cost - (num_children * child_ticket_cost)) / num_adults
    result = adult_ticket_cost
    return result

print(solution())