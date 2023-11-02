def solution():
    
    starting_population = 684
    population_increase = starting_population * 0.25
    new_population = starting_population + population_increase
    population_migration = new_population * 0.4
    current_population = new_population - population_migration
    result = current_population
    return result

print(solution())