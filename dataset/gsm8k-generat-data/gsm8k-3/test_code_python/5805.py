def solution():
    """Youngsville had a population of 684 people.  The town had a growth spurt and the population increased by 25% then they witnessed that 40% of the population moved away.  What is the current population?"""
    # Define the initial population of Youngsville
    initial_population = 684

    # Calculate the population after the growth spurt
    population_after_growth = initial_population * 1.25

    # Calculate the population after 40% of the population moved away
    current_population = population_after_growth * 0.6

    # Display the current population
    result = current_population
    return result

print(solution())