def solution():
    """The population of Mojave was 4000 a decade ago. If the town's population has increased three times, and the population analysis firm predicts that it will increase by 40% after five years, how many people will be in Mojave in five years?"""
    starting_population = 4000
    current_population = starting_population * 3 # population increased three times
    growth_rate = 0.4
    population_in_five_years = current_population * (1 + growth_rate)
    result = population_in_five_years
    return result

print(solution())