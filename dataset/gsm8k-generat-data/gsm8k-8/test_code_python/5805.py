def solution():
    # Define the initial population and growth rate
    initial_population = 684
    growth_rate = 0.25

    # Calculate the new population after the growth spurt
    new_population = initial_population + (growth_rate * initial_population)

    # Calculate the population after people moved away
    final_population = new_population - (0.4 * new_population)

    result = final_population
    return result

print(solution())