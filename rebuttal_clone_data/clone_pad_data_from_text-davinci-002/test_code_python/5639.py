def solution():
    
    stadiums_per_year = 30
    travel_cost_per_stadium = 900
    savings_per_year = 1500
    
    years_needed = travel_cost_per_stadium * stadiums_per_year / savings_per_year
    
    result = years_needed
    return result

print(solution())