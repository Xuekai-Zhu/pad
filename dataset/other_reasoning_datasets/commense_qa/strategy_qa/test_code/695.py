def solution():
    sartre_birth_year = 1905
    elizabeth_death_year = 1603
    if elizabeth_death_year < sartre_birth_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())