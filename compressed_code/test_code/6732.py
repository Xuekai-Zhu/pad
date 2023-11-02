def solution():
    
    isabelle_ticket = 20
    brothers_ticket = 10
    total_ticket_cost = isabelle_ticket + (2 * brothers_ticket)
    saved_money = 5 + 5
    job_pay_per_week = 3
    weeks_to_afford = (total_ticket_cost - saved_money) / job_pay_per_week
    result = weeks_to_afford
    return result

print(solution())