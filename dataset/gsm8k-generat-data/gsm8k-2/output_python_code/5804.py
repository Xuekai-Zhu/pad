def solution():
    """Youngsville had a population of 684 people. The town had a growth spurt and the population increased by 25% then they witnessed that 40% of the population moved away. What is the current population?"""
    starting_population = 684
    population_increase = starting_population * 0.25
    new_population = starting_population + population_increase
    population_migration = new_population * 0.4
    current_population = new_population - population_migration
    result = current_population
    return result

print(solution())