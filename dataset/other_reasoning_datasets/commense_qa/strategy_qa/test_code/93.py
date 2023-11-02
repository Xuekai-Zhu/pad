def solution():
    daily_mirror_founded_year = 1903
    shakespeare_death_year = 1616
    if daily_mirror_founded_year > shakespeare_death_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())