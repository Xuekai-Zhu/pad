def solution():
    """Mr. Roberts can buy a television for $400 cash or $120 down payment and $30 a month for 12 months. How much can he save by paying cash?"""
    # Define the cost of the television
    tv_cost = 400

    # Define the cost of the television under the payment plan
    plan_cost = 120 + 30*12

    # Calculate the amount saved by paying cash
    savings = plan_cost - tv_cost

    result = savings
    return result

print(solution())