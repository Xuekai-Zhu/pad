def solution():
    """ Salem is 15 times the size of Leesburg. Leesburg has 58940 people. If 130000 people move out of Salem, and half of Salem's population is women, how many women live in Salem?"""
    # Define the initial population of Leesburg and the ratio of Salem to Leesburg
    leesburg_population = 58940
    salem_ratio = 15

    # Calculate the population of Salem
    salem_population = salem_ratio * leesburg_population

    # Calculate the new population of Salem after 130000 people move out
    salem_population_new = salem_population - 130000

    # Calculate the number of women in Salem
    women_population = salem_population_new / 2

    # Return the result
    result = women_population
    return result

print(solution())