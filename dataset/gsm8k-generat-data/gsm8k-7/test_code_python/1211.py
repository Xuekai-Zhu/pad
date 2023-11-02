def solution():
    isabelle_ticket_cost = 20
    brothers_ticket_cost = 10
    brothers_savings = 5
    total_savings = 10

    total_cost = isabelle_ticket_cost + (2 * (brothers_ticket_cost - brothers_savings))
    amount_needed = total_cost - total_savings

    weeks_needed = amount_needed / 3
    result = weeks_needed
    return result

print(solution())