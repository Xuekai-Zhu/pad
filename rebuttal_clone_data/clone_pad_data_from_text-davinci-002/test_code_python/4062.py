def solution():
    ticket_price = 181
    drink_ticket_price = 7
    drink_tickets = 5
    total_price = ticket_price + (drink_ticket_price * drink_tickets)
    hours_worked_per_week = 30
    hourly_wage = 18
    weeks_in_month = 4
    monthly_salary = hours_worked_per_week * hourly_wage * weeks_in_month
    total_percentage = total_price / monthly_salary
    result = total_percentage
    return result

print(solution())