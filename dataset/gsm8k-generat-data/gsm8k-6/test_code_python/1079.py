def solution():
    # Calculate the total cost of the television if Mr. Roberts chooses the payment plan
    payment_plan_cost = 120 + (30 * 12)  # $120 down payment and $30 a month for 12 months
    # Calculate the amount saved by paying cash
    savings = payment_plan_cost - 400  # television costs $400 if paid in cash
    result = savings
    return result

print(solution())