def solution():
    concert_ticket_cost = 181
    num_drink_tickets = 5
    drink_ticket_cost = 7
    hourly_wage = 18
    weekly_hours_worked = 30
    days_in_month = 30

    # Calculate the total cost of the outing
    total_cost = concert_ticket_cost + (num_drink_tickets * drink_ticket_cost)

    # Calculate Jenna's weekly earnings
    weekly_earnings = hourly_wage * weekly_hours_worked

    # Calculate Jenna's monthly earnings
    monthly_earnings = weekly_earnings * 4

    # Calculate the percentage of Jenna's monthly salary spent on the outing
    percentage_spent = (total_cost / monthly_earnings) * 100
    result = percentage_spent
    return result

print(solution())