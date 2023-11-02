def solution():
    
    monthly_income = 20 + 40
    monthly_savings = 0.5 * monthly_income
    target_savings = 150
    months_needed = target_savings / monthly_savings
    result = months_needed
    return result

print(solution())