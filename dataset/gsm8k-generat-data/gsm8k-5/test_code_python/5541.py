def solution():
    num_adults = 5
    num_children = 2
    cost_concessions = 12
    total_cost = 76
    child_ticket_cost = 7

    # Calculate the cost of the adult tickets
    total_tickets_cost = total_cost - cost_concessions - (num_children * child_ticket_cost)
    adult_ticket_cost = total_tickets_cost / num_adults
    result = adult_ticket_cost
    return result

print(solution())