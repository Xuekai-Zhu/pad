def solution():
    """Joanie wants to join a gym to get into shape. The gym costs $12 per month and has a $50 down payment. How much will she need to pay for the first 3 years?"""
    # Define the cost of the gym membership per month and the down payment
    MEMBERSHIP_COST = 12
    DOWN_PAYMENT = 50

    # Calculate the cost of the gym membership for the first 3 years
    total_months = 3 * 12 # 3 years = 36 months
    monthly_cost = MEMBERSHIP_COST * total_months
    total_cost = monthly_cost + DOWN_PAYMENT

    # Display the total cost
    result = total_cost
    return result

print(solution())