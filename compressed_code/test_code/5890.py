def solution():
    
    adult_ticket_cost = 109
    child_ticket_cost = adult_ticket_cost - 5
    num_adults = 2
    num_children = 2
    total_cost = (adult_ticket_cost * num_adults) + (child_ticket_cost * num_children)
    amount_paid = 500
    change = amount_paid - total_cost
    result = change
    return result

print(solution())