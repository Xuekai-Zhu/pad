def solution():
    # Calculate the initial population of Salem
    leesburg_population = 58940
    salem_population = 15 * leesburg_population

    # Calculate the new population of Salem after people move out
    salem_population -= 130000

    # Calculate the number of women in Salem
    women_population = salem_population // 2
    result = women_population
    return result

print(solution())