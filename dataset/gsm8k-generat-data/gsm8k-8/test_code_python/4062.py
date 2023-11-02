def solution():
    # Calculate the total cost of the outing
    ticket_cost = 181
    drink_cost = 5 * 7
    total_cost = ticket_cost + drink_cost

    # Calculate Jenna's hourly and monthly salary
    hourly_salary = 18
    weekly_hours = 30
    monthly_salary = hourly_salary * weekly_hours * 4

    # Calculate the percentage of her monthly salary that she will spend
    percentage_spent = (total_cost / monthly_salary) * 100
    result = percentage_spent
    return result

print(solution())