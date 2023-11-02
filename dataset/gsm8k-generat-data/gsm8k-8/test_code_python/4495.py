def solution():
    # Define the starting population and growth rate
    starting_population = 100000
    growth_rate = 0.6

    # Calculate the population after 10 years of growth
    population_after_growth = starting_population * (1 + growth_rate) ** 10

    # Calculate the net migration rate
    net_migration_rate = 2500 - 2000

    # Calculate the total migration over 10 years
    total_migration = net_migration_rate * 10

    # Calculate the population after migration
    population_after_migration = population_after_growth + total_migration

    result = population_after_migration
    return result

print(solution())