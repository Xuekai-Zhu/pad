def solution():
    # Calculate the total cost of the outing
    concert_ticket_cost = 181
    drink_ticket_cost = 5 * 7
    total_cost = concert_ticket_cost + drink_ticket_cost

    # Calculate Jenna's monthly salary
    hourly_salary = 18
    weekly_hours = 30
    monthly_salary = hourly_salary * weekly_hours * 4

    # Calculate the percentage of Jenna's monthly salary spent on the outing
    percentage_spent = (total_cost / monthly_salary) * 100
    result = percentage_spent
    return result

print(solution())