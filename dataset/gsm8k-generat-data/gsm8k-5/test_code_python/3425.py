def solution():
    current_population = 4000  # The current population of Mojave is 4000
    increased_population = current_population * 3  # The town's population has increased three times
    predicted_increase = 0.4  # The population analysis firm predicts a 40% increase after 5 years

    # Calculate the population after 5 years
    population_after_5_years = increased_population + (increased_population * predicted_increase)

    result = population_after_5_years
    return result

print(solution())