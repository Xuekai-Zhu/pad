def solution():
    mozart_death_year = 1791
    wagner_birth_year = 1813
    if mozart_death_year < wagner_birth_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())