def solution():
    # Define ages of Methuselah and Jeanne Louise Calment
    methuselah_age = 969
    calment_age = 122.5
    # Define start and end years of Common Era
    common_era_start = 1
    common_era_end = 2021
    # Calculate Methuselah's birth year and check if it is within the Common Era
    methuselah_birth_year = common_era_start - methuselah_age
    if methuselah_birth_year > 0 and methuselah_birth_year < common_era_end:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())