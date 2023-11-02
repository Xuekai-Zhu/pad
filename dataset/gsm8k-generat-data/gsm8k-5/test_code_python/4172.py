def solution():
    # Calculate the cost of adult tickets
    adult_tickets = 9
    adult_ticket_cost = 11
    total_adult_cost = adult_tickets * adult_ticket_cost

    # Calculate the cost of children's tickets
    children_tickets = 7
    children_ticket_cost = 7
    total_children_cost = children_tickets * children_ticket_cost

    # Calculate the difference in total cost
    cost_difference = total_adult_cost - total_children_cost
    result = cost_difference
    return result

print(solution())