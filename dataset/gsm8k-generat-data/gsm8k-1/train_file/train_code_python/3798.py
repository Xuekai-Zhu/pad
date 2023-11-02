def solution():
    """In four years, Suzy will be twice Mary's age then. If Suzy is 20 now, how old is Mary?"""
    suzy_age_now = 20
    years = 4
    twice_mary_age_in_years = suzy_age_now + years * 2
    mary_age_in_years = twice_mary_age_in_years / 2
    result = mary_age_in_years
    return result

print(solution())