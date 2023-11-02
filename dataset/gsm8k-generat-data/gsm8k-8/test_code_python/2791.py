def solution():
    # Calculate the cost of one adult ticket and one child ticket
    adult_ticket_cost = 35
    child_ticket_cost = 20

    # Calculate the total cost of adult tickets and children's tickets
    total_adult_cost = 1 * adult_ticket_cost
    total_child_cost = 6 * child_ticket_cost

    # Calculate the total cost of buying tickets separately
    total_cost = total_adult_cost + total_child_cost

    result = total_cost
    return result

print(solution())