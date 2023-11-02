def solution():
    """If Beth is 18 years old and her little sister is 5, in how many years would she be twice her sister's age?"""
    beth_age = 18
    sister_age = 5
    age_diff = beth_age - sister_age
    years_needed = age_diff
    while (beth_age + years_needed) / (sister_age + years_needed) != 2:
        years_needed += 1

    result = years_needed
    return result

print(solution())