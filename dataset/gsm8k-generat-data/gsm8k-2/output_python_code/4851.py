def solution():
    """A newspaper subscription costs $10/month. If you purchase an annual subscription you obtain a 20% discount on your total bill. How much do you end up paying if you go with the annual subscription?"""
    monthly_cost = 10
    annual_cost = monthly_cost * 12
    discount = 0.2
    total_discount = annual_cost * discount
    discounted_annual_cost = annual_cost - total_discount
    result = discounted_annual_cost
    return result

print(solution())