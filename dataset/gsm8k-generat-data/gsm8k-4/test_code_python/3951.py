def solution():
    """Kelsey turned 25 in 1999. Her older sister was born 3 years before Kelsey. It's currently 2021. How old is Kelsey's older sister?"""
    # Calculate the year Kelsey was born
    kelsey_birth_year = 1999 - 25

    # Calculate the year Kelsey's sister was born
    sister_birth_year = kelsey_birth_year - 3

    # Calculate Kelsey's sister's age in 2021
    sister_age = 2021 - sister_birth_year

    # Return the result
    result = sister_age
    return result

print(solution())