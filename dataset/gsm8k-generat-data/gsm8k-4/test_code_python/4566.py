def solution():
    """Zion is 8 years old and his dad is 3 more than 4 times his age. In 10 years, how many years older is Zion's dad than him?"""
    # Define Zion's age
    zion_age = 8

    # Calculate Zion's dad's age
    dad_age = 4 * zion_age + 3

    # Calculate the age difference in 10 years
    age_diff_in_10_years = dad_age - (zion_age + 10)

    # return the result
    result = age_diff_in_10_years
    return result

print(solution())