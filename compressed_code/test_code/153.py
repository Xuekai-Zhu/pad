def solution():
    
    total_months = 24
    monthly_savings = 25
    total_savings = total_months * monthly_savings
    car_repair_cost = 400
    remaining_savings = total_savings - car_repair_cost
    result = remaining_savings
    return result

print(solution())