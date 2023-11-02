def solution():
    initial_population = 684
    growth_rate = 0.25
    emigration_rate = 0.4

    # Calculate the new population after growth
    new_population = initial_population + (initial_population * growth_rate)

    # Calculate the population after emigration
    current_population = new_population - (new_population * emigration_rate)
    result = current_population
    return result

print(solution())