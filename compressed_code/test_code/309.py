def solution():
    
    current_savings = 3000
    monthly_savings = 276
    saving_years = 4
    total_savings = current_savings + (monthly_savings * saving_years * 12) + 7000
    result = total_savings
    return result

print(solution())