def solution():
    compact_disc_release_year = 1982
    john_lennon_death_year = 1980
    if john_lennon_death_year < compact_disc_release_year:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())