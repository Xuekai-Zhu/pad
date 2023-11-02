def solution():
    
    ticket_cost = 181
    drink_tickets = 5
    drink_ticket_price = 7
    total_cost = ticket_cost + (drink_tickets * drink_ticket_price)
    hourly_salary = 18
    weekly_work_hours = 30
    monthly_salary = hourly_salary * weekly_work_hours * 4
    percentage_spent = (total_cost / monthly_salary) * 100
    result = percentage_spent
    return result

print(solution())