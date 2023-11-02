def solution():
    bonanza_start_year = 1959
    gandhi_death_year = 1948
    if gandhi_death_year < bonanza_start_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())