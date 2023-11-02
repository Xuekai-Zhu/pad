def solution():
    original_population = 1000
    new_population = 100
    population_change = 400
    current_population = original_population + new_population + population_change
    population_after_1_year = current_population / 2
    population_after_2_years = population_after_1_year / 2
    population_after_3_years = population_after_2_years / 2
    population_after_4_years = population_after_3_years / 2
    result = population_after_4_years
    return result

print(solution())