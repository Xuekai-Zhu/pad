def solution():
    
    initial_population = 100000
    percent_increase = 60
    population_increase = initial_population * (percent_increase / 100)
    final_population = initial_population + population_increase
    net_migration = (2500 - 2000) * 10
    total_population = final_population + net_migration
    result = total_population
    return result

print(solution())