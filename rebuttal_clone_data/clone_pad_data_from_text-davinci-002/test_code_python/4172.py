def solution():
    adults = 9
    children = 7
    adult_ticket_cost = 11
    child_ticket_cost = 7
    adults_total_cost = adults * adult_ticket_cost
    children_total_cost = children * child_ticket_cost
    difference = adults_total_cost - children_total_cost
    result = difference
    return result

print(solution())