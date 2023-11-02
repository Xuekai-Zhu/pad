def solution():
    """A city has a population of 300,000. 50,000 people immigrate to the country and then 30,000 people leave. After that 1/8 of the population gets pregnant and 1/4 of those people have twins. How many people are there after the births?"""
    # Define the initial population
    population = 300000

    # Calculate the net migration
    net_migration = 50000 - 30000

    # Adjust the population for net migration
    population += net_migration

    # Calculate the number of people who get pregnant
    pregnant = population // 8

    # Calculate the number of people who have twins
    twins = pregnant // 4

    # Adjust the population for births
    population += twins * 2

    # Return the final population count
    result = population
    return result

print(solution())