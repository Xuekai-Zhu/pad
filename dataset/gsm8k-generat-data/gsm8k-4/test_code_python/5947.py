def solution():
    """Karina was born in 1970 and she is currently twice as old as her brother. If her current age is 40, in what year was her brother born?"""
    # Define Karina's birth year and her current age
    KARINA_BIRTH_YEAR = 1970
    KARINA_CURRENT_AGE = 40

    # Calculate her brother's current age
    brother_current_age = KARINA_CURRENT_AGE / 2

    # Calculate her brother's birth year
    brother_birth_year = KARINA_BIRTH_YEAR + (KARINA_CURRENT_AGE - brother_current_age)

    # Subtract the brother's age from Karina's birth year to find the year of his birth
    brother_birth_year = KARINA_BIRTH_YEAR - brother_current_age

    result = brother_birth_year
    return result

print(solution())