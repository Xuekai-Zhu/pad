def solution():
    malcolm_x_birth_year = 1925
    malcolm_x_death_year = 1965
    unicode_standard_year = 1991
    if malcolm_x_birth_year < unicode_standard_year and malcolm_x_death_year < unicode_standard_year:
        result = "no"
    else:
        result = "uncertain"
    return result

print(solution())