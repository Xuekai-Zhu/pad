def solution():
    """The population of an area starts at 100,000 people. It increases by 60% over 10 years due to birth. In that same time, 2000 people leave per year from emigration and 2500 people come in per year from immigration. How many people are in the area at the end of 10 years?"""
    # Define the initial population and the number of years
    initial_population = 100000
    years = 10

    # Calculate the total number of people leaving and coming to the area over 10 years
    net_migration = (2500 - 2000) * years

    # Calculate the population growth due to birth
    growth_factor = 1 + 0.6
    final_population = initial_population * (growth_factor ** years)

    # Add in the net migration to get the final population
    final_population += net_migration

    # return the result
    result = final_population
    return result

print(solution())