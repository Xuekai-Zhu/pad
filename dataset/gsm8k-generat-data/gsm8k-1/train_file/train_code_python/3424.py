def solution():
    """The population of Mojave was 4000 a decade ago. If the town's population has increased three times, and the population analysis firm predicts that it will increase by 40% after five years, how many people will be in Mojave in five years?"""
    initial_population = 4000
    population_increase = 3
    current_population = initial_population * population_increase

    predicted_increase = 40
    predicted_population = current_population * (1 + (predicted_increase / 100))

    result = predicted_population
    return result

print(solution())