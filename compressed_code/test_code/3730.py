def solution():
    
    monthly_cost = 12
    down_payment = 50
    years = 3
    total_months = years * 12
    cost_per_month = monthly_cost + down_payment / total_months
    total_cost = cost_per_month * total_months
    result = total_cost
    return result

print(solution())