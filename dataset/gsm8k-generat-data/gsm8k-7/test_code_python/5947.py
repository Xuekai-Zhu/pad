def solution():
    karina_age = 40
    karina_birth_year = 1970

    # Calculate the birth year of Karina's brother
    brother_age = karina_age / 2
    brother_birth_year = karina_birth_year + (karina_age - brother_age)

    # Calculate the year when Karina's brother was born
    brother_birth_year += 1  # assuming he was born before the current year
    result = brother_birth_year
    return result

print(solution())