def solution():
    
    cost_of_shoes = 120
    current_savings = 30
    earnings_per_weekend = 15  
    weeks_needed = (cost_of_shoes - current_savings) / earnings_per_weekend
    result = weeks_needed
    return result

print(solution())