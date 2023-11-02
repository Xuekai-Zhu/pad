def solution():
    """There are 3/5 times as many people living in Boise as the number living in Seattle. There are 4000 more people in Lake View than the population in Seattle. If Lake View's population is 24000, calculate the total population of the three cities."""
    # Calculate the population of Seattle
    seattle_population = (24000 - 4000) * 5 / 3

    # Calculate the population of Boise
    boise_population = seattle_population * 3 / 5

    # Calculate the total population of the three cities
    total_population = seattle_population + boise_population + 24000

    # Display the total population
    result = total_population
    return result

print(solution())