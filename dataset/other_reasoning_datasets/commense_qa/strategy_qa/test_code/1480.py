def solution():
    avicenna_birth_year = 980
    al_farabi_death_year = 950
    if al_farabi_death_year < avicenna_birth_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())