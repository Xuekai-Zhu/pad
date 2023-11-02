def solution():
    
    starting_population = 4000
    current_population = starting_population * 3 
    growth_rate = 0.4
    population_in_five_years = current_population * (1 + growth_rate)
    result = population_in_five_years
    return result

print(solution())