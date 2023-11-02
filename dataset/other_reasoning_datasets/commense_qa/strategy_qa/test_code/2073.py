def solution():
    olympics_year = 1936
    berlin_wall_construction_year = 1961
    if berlin_wall_construction_year > olympics_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())