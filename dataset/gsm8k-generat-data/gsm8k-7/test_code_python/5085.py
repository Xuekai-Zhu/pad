def solution():
    leesburg_population = 58940
    salem_size_factor = 15

    # Calculate Salem's population based on Leesburg's population
    salem_population = leesburg_population * salem_size_factor

    # Calculate Salem's population after 130000 people move out
    salem_population_after_move = salem_population - 130000

    # Calculate the number of women in Salem
    num_women = salem_population_after_move / 2
    result = num_women
    return result

print(solution())