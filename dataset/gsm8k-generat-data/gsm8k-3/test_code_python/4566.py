def solution():
    """Zion is 8 years old and his dad is 3 more than 4 times his age. In 10 years, how many years older is Zion's dad than him?"""
    # Define Zion's age and his dad's age
    zion_age = 8
    dad_age = 4 * zion_age + 3

    # Calculate how old they will be in 10 years
    zion_in_10_years = zion_age + 10
    dad_in_10_years = dad_age + 10

    # Calculate the age difference in 10 years
    age_difference = dad_in_10_years - zion_in_10_years

    # Display the age difference
    result = age_difference
    return result

print(solution())