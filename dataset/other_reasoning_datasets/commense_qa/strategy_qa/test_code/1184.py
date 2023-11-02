def solution():
    ps4_launch_year = 2013
    tom_bosley_death_year = 2010
    if tom_bosley_death_year < ps4_launch_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())