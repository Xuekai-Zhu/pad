def solution():
    concert_ticket_cost = 181  # Jenna wants to buy a concert ticket that costs $181
    drink_ticket_cost = 7  # Jenna wants to buy 5 drink tickets for $7 each
    total_cost = concert_ticket_cost + (5 * drink_ticket_cost)  # Jenna's total cost for the outing
    hourly_rate = 18  # Jenna earns $18 per hour
    weekly_hours = 30  # Jenna works 30 hours per week
    monthly_salary = hourly_rate * weekly_hours * 4  # Jenna's monthly salary

    # Calculate the percentage of Jenna's monthly salary that she will spend on this outing
    percentage_spent = (total_cost / monthly_salary) * 100
    result = percentage_spent
    return result

print(solution())