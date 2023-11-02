def solution():
    population = 50  # The population of porcupines in the park is 50
    female_population = (3/5) * population  # The number of female porcupines is 3/5 of the total population
    babies_per_month = 4  # Each female porcupine gives birth to 4 babies every month
    months_per_year = 12  # There are 12 months in a year

    # Calculate the total number of porcupines in the park after a year
    total_porcupines = population + female_population * babies_per_month * months_per_year
    result = total_porcupines
    return result

print(solution())