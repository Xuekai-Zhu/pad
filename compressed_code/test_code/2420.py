def solution():
    
    adult_ticket_price = 11
    child_ticket_price = 8
    senior_ticket_price = 9
    num_adults = 2
    num_children = 3
    num_seniors = 2
    adult_total_price = num_adults * adult_ticket_price
    child_total_price = num_children * child_ticket_price
    senior_total_price = num_seniors * senior_ticket_price
    total_price = adult_total_price + child_total_price + senior_total_price
    result = total_price
    return result

print(solution())