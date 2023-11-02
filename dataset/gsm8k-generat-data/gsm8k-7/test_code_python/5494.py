def solution():
    adult_ticket_cost = 8
    child_ticket_cost = 3
    available_funds = 35

    # Determine the maximum number of children that can go with the adult, based on available funds and ticket prices
    max_children = (available_funds - adult_ticket_cost) / child_ticket_cost

    result = max_children
    return result

print(solution())