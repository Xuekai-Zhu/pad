def solution():
    """The population of Mojave was 4000 a decade ago. If the town's population has increased three times, and the population analysis firm predicts that it will increase by 40% after five years, how many people will be in Mojave in five years?"""
    # Define the current population and the population increase factor
    current_population = 4000
    population_increase = 3

    # Calculate the population after the first increase
    population_after_increase = current_population * population_increase

    # Calculate the population after the predicted increase in five years
    population_in_five_years = population_after_increase * 1.4

    # Display the population in five years
    result = population_in_five_years
    return result

print(solution())