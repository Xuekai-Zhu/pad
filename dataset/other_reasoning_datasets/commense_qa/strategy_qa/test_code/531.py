def solution():
    university_creation_year = 1696
    baroque_period_start_year = 1600
    baroque_period_end_year = 1750
    if university_creation_year >= baroque_period_start_year and university_creation_year <= baroque_period_end_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())