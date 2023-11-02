def solution():
    """The population of an area starts at 100,000 people. It increases by 60% over 10 years due to birth. In that same time, 2000 people leave per year from emigration and 2500 people come in per year from immigration. How many people are in the area at the end of 10 years?"""
    initial_population = 100000
    percent_increase = 60
    population_increase = initial_population * (percent_increase / 100)
    final_population = initial_population + population_increase
    net_migration = (2500 - 2000) * 10
    total_population = final_population + net_migration
    result = total_population
    return result

print(solution())