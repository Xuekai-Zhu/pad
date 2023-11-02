def solution():
    ivan_death_year = 1584
    first_flight_year = 1783
    if ivan_death_year < first_flight_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())