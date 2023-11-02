def solution():
    # Find the population of Seattle
    population_Seattle = (24000 - 4000) / (3/5)  

    # Find the population of Boise
    population_Boise = (3/5) * population_Seattle  

    # Calculate the total population of the three cities
    total_population = population_Seattle + population_Boise + 24000
    result = total_population
    return result

print(solution())