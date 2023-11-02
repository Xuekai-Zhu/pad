def solution():
    alexander_hamilton_death_year = 1804
    koala_first_depiction_year = 1810
    if koala_first_depiction_year > alexander_hamilton_death_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())