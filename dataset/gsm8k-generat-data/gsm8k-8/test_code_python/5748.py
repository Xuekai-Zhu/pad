def solution():
    # Calculate the population of Seattle
    seattle_population = (24000 - 4000) / (3/5)

    # Calculate the population of Boise
    boise_population = seattle_population * (3/5)

    # Calculate the total population of the three cities
    total_population = seattle_population + boise_population + 24000
    result = total_population
    return result

print(solution())