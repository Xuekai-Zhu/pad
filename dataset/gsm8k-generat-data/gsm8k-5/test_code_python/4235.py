def solution():
    final_population = 60  # After 4 years, the population is 60 people
    population_after_outflow = final_population * 2  # The population after the outflow is double the final population
    population_after_inflow = population_after_outflow + 100 - 400  # The population after the inflow is the outflow subtracted from the inflow and added to the population after the outflow

    # Calculate the initial population before the new people moved in
    initial_population = population_after_inflow / (2 ** 4)  # The population is halved every year for 4 years
    result = initial_population
    return result

print(solution())