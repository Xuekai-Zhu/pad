def solution():
    """There are 3/5 times as many people living in Boise as the number living in Seattle. There are 4000 more people in Lake View than the population in Seattle. If Lake View's population is 24000, calculate the total population of the three cities."""
    # Calculate the population of Seattle
    seattle_population = (24000 - 4000) / (3/5 + 1)

    # Calculate the population of Boise
    boise_population = 3/5 * seattle_population

    # Calculate the total population of the three cities
    total_population = seattle_population + boise_population + 24000

    # return the result
    result = total_population
    return result

print(solution())