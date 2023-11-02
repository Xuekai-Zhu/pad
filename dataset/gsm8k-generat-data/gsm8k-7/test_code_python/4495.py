def solution():
    population = 100000
    increase_rate = 0.6
    years = 10
    emigration = 2000
    immigration = 2500

    # Calculate the increase in population due to birth
    birth_increase = population * increase_rate

    # Calculate the total increase in population due to immigration
    immigration_increase = (immigration - emigration) * years

    # Calculate the total population at the end of 10 years
    total_population = population + birth_increase + immigration_increase
    result = total_population
    return result

print(solution())