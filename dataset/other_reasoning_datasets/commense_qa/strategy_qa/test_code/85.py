def solution():
    duke_birth_year = 1475
    war_start_year = 1337
    war_end_year = 1453
    if duke_birth_year > war_end_year or duke_birth_year < war_start_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())