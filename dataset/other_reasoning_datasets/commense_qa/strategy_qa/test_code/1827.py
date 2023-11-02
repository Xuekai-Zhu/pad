def solution():
    leap_year_period = 4
    chipmunk_lifespan = 3
    leap_years_in_chipmunk_lifespan = chipmunk_lifespan // leap_year_period
    if leap_years_in_chipmunk_lifespan < 2:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())