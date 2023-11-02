def solution():
    
    initial_length = 6
    final_length = 36
    growth_rate = 0.5
    growth_per_month = growth_rate * 12
    total_growth = final_length - initial_length
    total_months = total_growth / growth_rate
    total_years = total_months / 12
    result = total_years
    return result

print(solution())