def solution():
    # Calculate the population at the end of 4 years
    population = 60  # given
    for i in range(4):
        population *= 2  # halved every year

    # Reverse calculate the original population
    original_population = population + 400 - 100
    result = original_population
    return result

print(solution())