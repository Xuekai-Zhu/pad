def solution():
    """In 5 years, Nacho will be three times older than Divya. If Divya is currently 5 years old, what's the sum of their ages now?"""
    # Define Divya's current age
    divya_age = 5

    # Calculate Nacho's age in 5 years
    nacho_age_in_5_years = 3 * (divya_age + 5)

    # Calculate Nacho's current age
    nacho_age = nacho_age_in_5_years - 5

    # Calculate the sum of their current ages
    sum_of_ages = divya_age + nacho_age

    # return the result
    result = sum_of_ages
    return result

print(solution())