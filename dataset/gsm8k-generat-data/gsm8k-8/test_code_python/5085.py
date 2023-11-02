def solution():
    # Define the initial population of Leesburg and the ratio between Salem and Leesburg
    leesburg_population = 58940
    salem_to_leesburg_ratio = 15

    # Calculate the population of Salem
    salem_population = leesburg_population * salem_to_leesburg_ratio

    # Calculate the population of Salem after 130000 people move out
    salem_population_after_move = salem_population - 130000

    # Calculate the number of women in Salem
    women_in_salem = salem_population_after_move / 2

    result = women_in_salem
    return result

print(solution())