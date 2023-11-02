def solution():
    adult_count = 10
    child_count = 11
    adult_ticket_cost = 8
    total_cost = 124

    # Calculate the total cost of adult tickets
    adult_total_cost = adult_count * adult_ticket_cost

    # Calculate the cost of the children's tickets
    children_cost = total_cost - adult_total_cost

    # Calculate the cost of one child's ticket
    child_ticket_cost = children_cost / child_count
    result = child_ticket_cost
    return result

print(solution())