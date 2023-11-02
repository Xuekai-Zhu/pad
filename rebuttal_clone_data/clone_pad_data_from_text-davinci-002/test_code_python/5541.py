def solution():
    total_cost = 76
    cost_of_concessions = 12
    number_of_children = 2
    cost_of_child_ticket = 7
    cost_of_adult_tickets = total_cost - cost_of_concessions - (number_of_children * cost_of_child_ticket)
    result = cost_of_adult_tickets
    return result

print(solution())