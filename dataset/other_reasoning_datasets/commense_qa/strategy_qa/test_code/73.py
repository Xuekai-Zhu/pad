def solution():
    kant_death_year = 1804
    pierce_birth_year = 1804
    kant_death_month = "February"
    pierce_birth_month = "November"
    kant = False
    pierce = False
    if kant_death_year < pierce_birth_year:
        kant = True
    elif kant_death_year == pierce_birth_year and kant_death_month < pierce_birth_month:
        kant = True
    if kant and pierce:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())