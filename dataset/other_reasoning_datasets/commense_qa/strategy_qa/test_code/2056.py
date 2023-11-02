def solution():
    university_establishment_year = 1787
    millard_fillmore_birth_year = 1800
    if millard_fillmore_birth_year > university_establishment_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())