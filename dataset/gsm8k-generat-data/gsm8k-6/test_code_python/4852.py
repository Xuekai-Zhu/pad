def solution():
    # Calculate the total cost of an annual subscription
    monthly_cost = 10
    discounted_monthly_cost = 0.8 * monthly_cost
    annual_cost = 12 * discounted_monthly_cost  # 12 months in a year

    result = annual_cost
    return result

print(solution())