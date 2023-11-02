def solution():
    leap_year_frequency = 4
    bachelor_degree_duration = 4
    if bachelor_degree_duration % leap_year_frequency == 0:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())