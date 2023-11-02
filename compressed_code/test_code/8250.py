def solution():
    
    adult_ticket_price = 11
    child_ticket_price = 8
    senior_ticket_price = 9
    num_adults = 2
    num_children = 3
    num_seniors = 2
    total_cost = (num_adults * adult_ticket_price) + (num_children * child_ticket_price) + (num_seniors * senior_ticket_price)
    result = total_cost
    return result

print(solution())