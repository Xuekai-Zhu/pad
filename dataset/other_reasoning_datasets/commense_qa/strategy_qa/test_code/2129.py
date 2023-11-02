def solution():
    cane_toad_life_expectancy = 12.5 * 365 # convert to days
    hawaiian_male_life_expectancy = 79.3 * 365 # convert to days
    if hawaiian_male_life_expectancy > cane_toad_life_expectancy:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())