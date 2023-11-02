def solution():
    vip_ticket_cost = 100
    regular_ticket_cost = 50
    num_vip_tickets = 2
    num_regular_tickets = 3

    total_vip_cost = vip_ticket_cost * num_vip_tickets
    total_regular_cost = regular_ticket_cost * num_regular_tickets

    total_cost = total_vip_cost + total_regular_cost
    remaining_savings = 500 - total_cost

    result = remaining_savings
    return result

print(solution())