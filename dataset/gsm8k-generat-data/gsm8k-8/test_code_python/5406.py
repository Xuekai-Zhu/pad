def solution():
    # There are 3 children and 2 adults
    # Let x be the cost of a child ticket
    # Then the cost of an adult ticket is x+6

    total_cost = 77
    total_tickets = 5
    children_tickets = 3
    adult_tickets = total_tickets - children_tickets

    # From the given information, we have two equations:
    # child_tickets*x + adult_tickets*(x+6) = total_cost
    # child_tickets + adult_tickets = total_tickets

    # Substituting adult_tickets in terms of total_tickets and child_tickets:
    child_tickets = 3
    adult_tickets = total_tickets - child_tickets

    x = (total_cost - adult_tickets * 6) / child_tickets
    adult_ticket_cost = x + 6

    result = adult_ticket_cost
    return result

print(solution())