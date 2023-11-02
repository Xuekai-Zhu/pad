def solution():
    
    start_population = 450000
    end_population = 467000
    duration_years = 5
    average_growth_per_year = (end_population - start_population) / duration_years
    result = average_growth_per_year
    return result

print(solution())