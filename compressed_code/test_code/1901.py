def solution():
    
    num_adults = 1
    num_children = 3
    adult_ticket_price = 2
    child_ticket_price = 1
    total_cost = num_adults * adult_ticket_price + num_children * child_ticket_price
    change = 20 - total_cost
    result = change
    return result

print(solution())