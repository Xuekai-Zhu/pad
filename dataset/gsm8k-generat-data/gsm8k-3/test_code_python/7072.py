def solution():
    """In 5 years, Nacho will be three times older than Divya. If Divya is currently 5 years old, what's the sum of their ages now?"""
    # Calculate Divya's age in 5 years
    divya_age_5_years = 5 + 5

    # Calculate Nacho's age in 5 years
    nacho_age_5_years = 3 * divya_age_5_years

    # Calculate Nacho's current age
    nacho_current_age = nacho_age_5_years - 5

    # Calculate the sum of their ages now
    sum_of_ages = nacho_current_age + 5

    # Display the sum of their ages
    result = sum_of_ages
    return result

print(solution())