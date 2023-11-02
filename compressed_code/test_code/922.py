def solution():
    
    isabelle_ticket_cost = 20
    brother_ticket_cost = 10
    total_ticket_cost = isabelle_ticket_cost + 2 * brother_ticket_cost
    total_savings = 5 + 5
    remaining_cost = total_ticket_cost - total_savings
    weeks_to_work = remaining_cost / 3
    result = weeks_to_work
    return result

print(solution())