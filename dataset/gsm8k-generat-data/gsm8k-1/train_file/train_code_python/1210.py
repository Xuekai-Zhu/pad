def solution():
    """Isabelle gets a job so she can save enough money to go to a concert with her two brothers. Her ticket costs $20. Her brothers both get the children’s discount, and each of their tickets cost $10. Her brothers have saved $5 between the two of them and Isabelle has saved $5. If her job pays $3 per week, how many weeks must she work to afford the tickets?"""
    isabelle_ticket = 20
    brothers_ticket = 10
    total_ticket_cost = isabelle_ticket + (2 * brothers_ticket)
    saved_money = 5 + 5
    job_pay_per_week = 3
    weeks_to_afford = (total_ticket_cost - saved_money) / job_pay_per_week
    result = weeks_to_afford
    return result

print(solution())