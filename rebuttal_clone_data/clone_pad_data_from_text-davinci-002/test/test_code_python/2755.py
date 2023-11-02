def solution():
    monthly_cost = 10
    annual_discount = 20
    total_cost = monthly_cost * 12
    total_discount = total_cost * (annual_discount / 100)
    final_cost = total_cost - total_discount
    result = final_cost
    return result

print(solution())