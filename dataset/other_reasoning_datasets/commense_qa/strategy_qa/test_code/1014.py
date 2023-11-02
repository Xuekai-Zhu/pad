def solution():
    wagner_death_year = 1883
    tv_development_start_year = 1920
    if wagner_death_year < tv_development_start_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())