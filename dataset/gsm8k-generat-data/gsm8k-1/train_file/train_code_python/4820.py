def solution():
    """Joanie wants to join a gym to get into shape. The gym costs $12 per month and has a $50 down payment. How much will she need to pay for the first 3 years?"""
    monthly_cost = 12
    down_payment = 50
    time_period = 3 # in years
    total_months = time_period * 12
    total_cost = (total_months * monthly_cost) + down_payment
    result = total_cost
    return result

print(solution())