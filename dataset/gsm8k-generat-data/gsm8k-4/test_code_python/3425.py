def solution():
    """The population of Mojave was 4000 a decade ago. If the town's population has increased three times,
    and the population analysis firm predicts that it will increase by 40% after five years, how many people will
    be in Mojave in five years?"""
    # Define the initial population
    initial_population = 4000

    # Calculate the current population
    current_population = initial_population * 3

    # Calculate the predicted population after five years
    predicted_population = current_population * 1.4

    # return the result
    result = predicted_population
    return result

print(solution())