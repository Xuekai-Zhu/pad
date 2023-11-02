def solution():
    population = 684
    population_increase = population * 0.25
    new_population = population + population_increase
    population_decrease = new_population * 0.4
    current_population = new_population - population_decrease
    result = current_population
    return result

print(solution())