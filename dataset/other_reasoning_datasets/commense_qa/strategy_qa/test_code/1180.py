def solution():
    debut_year = 1993
    bruise_brody_death_year = 1988
    if bruise_brody_death_year < debut_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())