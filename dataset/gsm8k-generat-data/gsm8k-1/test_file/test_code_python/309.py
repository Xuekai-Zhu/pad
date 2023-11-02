def solution():
    """Six years ago, when Noah was half as old as Cera, the population of Chile was half what it is now. Currently, Cera is 46 years old. If the population of Chile six years ago was 3000 times the age of Noah, calculate the population of Chile now."""
    cera_age_six_years_ago = 46 - 6
    noah_age_six_years_ago = cera_age_six_years_ago / 2
    population_six_years_ago = noah_age_six_years_ago * 3000
    current_population = population_six_years_ago * 2
    result = current_population
    return result

print(solution())