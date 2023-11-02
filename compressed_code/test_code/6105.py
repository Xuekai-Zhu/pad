def solution():
    
    initial_savings = 3000
    monthly_savings = 276
    savings_duration = 4  
    family_contribution = 7000
    
    total_savings = initial_savings + (monthly_savings * 12 * savings_duration) + family_contribution
    
    result = total_savings
    
    return result

print(solution())