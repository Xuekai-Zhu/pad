def solution():
    
    adult_tickets = 9
    child_tickets = 7
    adult_price = 11
    child_price = 7
    adult_cost = adult_tickets * adult_price
    child_cost = child_tickets * child_price
    cost_difference = adult_cost - child_cost
    result = cost_difference
    return result

print(solution())