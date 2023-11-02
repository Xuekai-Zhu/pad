def solution():
    
    monthly_cost = 10
    annual_cost = monthly_cost * 12
    discount = 0.2
    total_discount = annual_cost * discount
    discounted_annual_cost = annual_cost - total_discount
    result = discounted_annual_cost
    return result

print(solution())