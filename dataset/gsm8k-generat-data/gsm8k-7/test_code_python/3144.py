def solution():
    investment_amount = 90
    time_period = 5  # in months

    # Jason earned twice his investment amount over 5 months, so his earnings per month are half his investment amount
    monthly_return = investment_amount / (2 * time_period)

    result = monthly_return
    return result

print(solution())