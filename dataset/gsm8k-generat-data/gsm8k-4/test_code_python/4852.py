def solution():
    """A newspaper subscription costs $10/month. If you purchase an annual subscription you obtain a 20% discount on your total bill. How much do you end up paying if you go with the annual subscription?"""
    # Define the cost of a monthly subscription
    monthly_cost = 10

    # Calculate the cost of an annual subscription with discount
    annual_cost = monthly_cost * 12 * 0.8

    result = annual_cost
    return result

print(solution())