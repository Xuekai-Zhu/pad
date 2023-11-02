def solution():
    """Jenna wants to buy a concert ticket that costs $181, plus five drink tickets for $7 each. If Jenna earns $18 an hour and works 30 hours a week, what percentage of her monthly salary will she spend on this outing?"""
    # Define the cost of the concert ticket and drink tickets
    CONCERT_TICKET = 181
    DRINK_TICKET = 7
    NUM_DRINK_TICKETS = 5

    # Calculate the total cost of the outing
    total_cost = CONCERT_TICKET + NUM_DRINK_TICKETS * DRINK_TICKET

    # Calculate Jenna's monthly salary
    WEEKS_PER_MONTH = 4
    hours_per_month = 30 * WEEKS_PER_MONTH
    monthly_salary = 18 * hours_per_month

    # Calculate the percentage of Jenna's monthly salary spent on the outing
    percentage_spent = total_cost / monthly_salary * 100

    # Display the percentage spent
    result = percentage_spent
    return result

print(solution())