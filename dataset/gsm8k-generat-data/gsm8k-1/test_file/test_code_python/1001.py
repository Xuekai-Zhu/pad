def solution():
    """The population of porcupines in a park is 50. The number of female porcupines is 3/5 of the total population.
    If each female porcupine gives birth to 4 babies every month, how many porcupines will be in the park after a year?"""
    total_population = 50
    female_porcupines = int(total_population * (3/5))
    babies_per_month = 4
    babies_per_year = babies_per_month * 12
    new_porcupines = female_porcupines * babies_per_year
    total_porcupines = total_population + new_porcupines
    result = total_porcupines
    return result

print(solution())