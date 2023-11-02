def solution():
    
    initial_population = 4000
    population_increase = 3
    current_population = initial_population * population_increase

    predicted_increase = 40
    predicted_population = current_population * (1 + (predicted_increase / 100))

    result = predicted_population
    return result

print(solution())