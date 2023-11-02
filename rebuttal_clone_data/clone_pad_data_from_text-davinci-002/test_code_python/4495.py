def solution():
    starting_pop = 100000
    percent_growth = 60
    emigration = 2000
    immigration = 2500
    growth_per_year = starting_pop * (percent_growth / 100)
    total_growth = growth_per_year * 10
    total_population = starting_pop + total_growth + (immigration - emigration) * 10
    result = total_population
    
    return result

print(solution())