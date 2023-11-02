def solution():
    adult_ticket_cost = 9
    child_ticket_cost = adult_ticket_cost - 2
    total_cost = 2 * adult_ticket_cost + child_ticket_cost
    cash_received = 20 + 20 - 1
    difference = cash_received - total_cost
    result = difference / -2
    return result

print(solution())