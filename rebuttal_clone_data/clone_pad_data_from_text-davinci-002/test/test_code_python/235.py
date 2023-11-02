def solution():
    savings = 500
    vip_tickets = 2
    regular_tickets = 3
    ticket_cost_vip = 100
    ticket_cost_regular = 50
    total_cost = vip_tickets * ticket_cost_vip + regular_tickets * ticket_cost_regular
    remaining_savings = savings - total_cost
    result = remaining_savings
    return result

print(solution())