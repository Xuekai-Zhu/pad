def solution():
    nypd_min_age = 21
    gen_y_birth_years = [1980, 1994]
    current_year = 2021
    oldest_gen_y_age = current_year - gen_y_birth_years[0]
    if oldest_gen_y_age >= nypd_min_age:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())