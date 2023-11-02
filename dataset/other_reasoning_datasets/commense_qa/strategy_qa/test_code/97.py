def solution():
    ada_age_at_death = 36
    life_expectancy_range = (35, 39)
    if ada_age_at_death < life_expectancy_range[0]:
        result = "yes"
    elif ada_age_at_death >= life_expectancy_range[0] and ada_age_at_death <= life_expectancy_range[1]:
        result = "it's possible"
    else:
        result = "no"
    return result

print(solution())