def solution():
    archduke_death_year = 1914
    pacific_war_start_year = 1941
    pacific_war_end_year = 1945
    if archduke_death_year < pacific_war_start_year:
        result = "no"
    elif archduke_death_year > pacific_war_end_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())