def solution():
    """In four years, Suzy will be twice Mary's age then. If Suzy is 20 now, how old is Mary?"""
    suzy_age = 20
    suzy_twice_mary_age = 2
    mary_age_4_years_ago = (suzy_age - 4) / suzy_twice_mary_age
    mary_current_age = mary_age_4_years_ago + 4
    result = mary_current_age
    return result

print(solution())