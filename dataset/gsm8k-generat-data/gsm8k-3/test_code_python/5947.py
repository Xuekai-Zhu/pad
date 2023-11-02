def solution():
    """Karina was born in 1970 and she is currently twice as old as her brother. If her current age is 40, in what year was her brother born?"""
    # Calculate Karina's birth year
    karina_birth_year = 1970

    # Calculate Karina's brother's current age
    brother_age = 40 / 2

    # Calculate Karina's brother's birth year
    brother_birth_year = 2021 - brother_age

    # Calculate the year in which Karina's brother was born
    year_brother_born = brother_birth_year - karina_birth_year

    # Display the year in which Karina's brother was born
    result = year_brother_born
    return result

print(solution())