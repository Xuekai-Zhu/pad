def solution():
    """Isabelle gets a job so she can save enough money to go to a concert with her two brothers. Her ticket costs $20. Her brothers both get the children’s discount, and each of their tickets cost $10. Her brothers have saved $5 between the two of them and Isabelle has saved $5. If her job pays $3 per week, how many weeks must she work to afford the tickets?"""
    isabelle_ticket_cost = 20
    brother_ticket_cost = 10
    total_ticket_cost = isabelle_ticket_cost + 2 * brother_ticket_cost
    total_savings = 5 + 5
    remaining_cost = total_ticket_cost - total_savings
    weeks_to_work = remaining_cost / 3
    result = weeks_to_work
    return result

print(solution())