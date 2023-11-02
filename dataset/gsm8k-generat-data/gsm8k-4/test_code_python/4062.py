def solution():
    """Jenna wants to buy a concert ticket that costs $181, plus five drink tickets for $7 each. If Jenna earns $18 an hour and works 30 hours a week, what percentage of her monthly salary will she spend on this outing?"""
    # Calculate the cost of the concert ticket and drink tickets
    ticket_cost = 181
    drink_cost = 5 * 7

    # Calculate the total cost of the outing
    total_cost = ticket_cost + drink_cost

    # Calculate Jenna's monthly salary
    hourly_salary = 18
    weekly_hours = 30
    monthly_salary = hourly_salary * weekly_hours * 4

    # Calculate the percentage of Jenna's monthly salary spent on the outing
    percentage = (total_cost / monthly_salary) * 100

    result = percentage
    return result

print(solution())