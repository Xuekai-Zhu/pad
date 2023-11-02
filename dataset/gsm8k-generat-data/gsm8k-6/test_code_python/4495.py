def solution():
    # Calculate the population after 10 years
    starting_pop = 100000
    birth_rate = 0.6
    emigration_rate = -2000
    immigration_rate = 2500
    net_migration = immigration_rate + emigration_rate
    population_growth = starting_pop * (1 + birth_rate) ** 10
    final_pop = population_growth + net_migration * 10
    
    result = final_pop
    return result

print(solution())