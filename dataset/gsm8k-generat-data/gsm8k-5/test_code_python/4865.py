def solution():
    population = 300000  # Initial population of the city
    immigration = 50000  # Number of people immigrating to the city
    emigration = 30000  # Number of people leaving the city
    net_population_change = immigration - emigration  # Net population change

    # Calculate the new population after immigration and emigration
    new_population = population + net_population_change

    # Calculate the number of people who get pregnant and have twins
    pregnant = new_population / 8
    twins = pregnant / 4

    # Calculate the final population after the births
    final_population = new_population + twins
    result = final_population
    return result

print(solution())