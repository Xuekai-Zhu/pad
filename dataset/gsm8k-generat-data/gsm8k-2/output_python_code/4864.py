def solution():
    """A city has a population of 300,000. 50,000 people immigrate to the country and then 30,000 people leave. After that 1/8 of the population gets pregnant and 1/4 of those people have twins. How many people are there after the births?"""
    initial_population = 300000
    immigration = 50000
    emigration = 30000
    population_after_migration = initial_population + immigration - emigration
    pregnancies = population_after_migration / 8
    twins = pregnancies / 4
    total_population = population_after_migration + twins
    result = total_population
    return result

print(solution())