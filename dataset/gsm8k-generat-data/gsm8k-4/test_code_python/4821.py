def solution():
    """Joanie wants to join a gym to get into shape. The gym costs $12 per month and has a $50 down payment. How much will she need to pay for the first 3 years?"""
    # Define the monthly cost and down payment
    MONTHLY_COST = 12
    DOWN_PAYMENT = 50

    # Calculate the total cost for the first year, including the down payment
    total_cost = DOWN_PAYMENT + (MONTHLY_COST * 12)

    # Calculate the total cost for the next two years
    total_cost += MONTHLY_COST * 24

    # return the result
    result = total_cost
    return result

print(solution())