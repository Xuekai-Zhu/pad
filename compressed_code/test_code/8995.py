def solution():
    
    concert_ticket_cost = 181
    drink_ticket_cost = 7
    num_drink_tickets = 5
    hours_worked_per_week = 30
    hourly_rate = 18
    weekly_salary = hours_worked_per_week * hourly_rate
    monthly_salary = weekly_salary * 4
    total_cost = concert_ticket_cost + (drink_ticket_cost * num_drink_tickets)
    percentage_of_monthly_salary = (total_cost / monthly_salary) * 100
    result = percentage_of_monthly_salary
    return result

print(solution())