def solution():
    num_adults = 5
    num_children = 2
    concessions_cost = 12
    total_cost = 76
    child_ticket_price = 7

    # Calculate the total cost of all tickets
    total_ticket_cost = total_cost - concessions_cost

    # Calculate the cost of all children's tickets
    children_ticket_cost = num_children * child_ticket_price

    # Calculate the cost of all adult tickets
    adult_ticket_cost = total_ticket_cost - children_ticket_cost

    # Calculate the cost of one adult ticket
    cost_of_one_adult_ticket = adult_ticket_cost / num_adults
    result = cost_of_one_adult_ticket
    return result

print(solution())