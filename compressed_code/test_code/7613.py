def solution():
    
    adult_ticket_cost = 4.25 + 3.25
    child_ticket_cost = 4.25
    num_adult_tickets = 2
    num_child_tickets = 4
    total_tickets = num_adult_tickets + num_child_tickets
    discount = 2
    total_cost = (adult_ticket_cost * num_adult_tickets) + (child_ticket_cost * num_child_tickets)
    if total_tickets > 3:
        total_cost -= discount
    result = total_cost
    return result

print(solution())