def solution():
    dc_comics_founded_year = 1934
    president_taft_death_year = 1930
    if dc_comics_founded_year > president_taft_death_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())