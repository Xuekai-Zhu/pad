def solution():
    """A newspaper subscription costs $10/month. If you purchase an annual subscription you obtain a 20% discount on your total bill. How much do you end up paying if you go with the annual subscription?"""
    # Define the monthly subscription cost
    MONTHLY_COST = 10

    # Calculate the cost of an annual subscription with discount
    annual_cost = 12 * MONTHLY_COST * 0.8

    # Display the total cost
    result = annual_cost
    return result

print(solution())