def solution():
     cost_of_shoes = 120
     Cary's_savings = 30
     earnings_per_lawn = 5
     lawns_per_weekend = 3
     
     money_needed = cost_of_shoes - Cary's_savings
     weekends_needed = money_needed / (earnings_per_lawn * lawns_per_weekend)
     
     result = weekends_needed
     
     return result

print(solution())