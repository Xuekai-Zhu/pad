def solution():
    # Calculate the population of Seattle
    population_seattle = (24000 - 4000) / (3/5)  # 3/5 times the population of Seattle is the population of Boise
    population_seattle = int(population_seattle)

    # Calculate the population of Boise
    population_boise = 3/5 * population_seattle
    population_boise = int(population_boise)

    # Calculate the total population of the three cities
    total_population = population_seattle + population_boise + 24000
    result = total_population
    return result

print(solution())