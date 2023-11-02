def solution():
    divya_age = 5  # Divya is currently 5 years old
    nacho_age_in_5_years = 3 * (divya_age + 5)  # Nacho will be three times older than Divya in 5 years
    nacho_age_now = nacho_age_in_5_years - 5  # Subtracting 5 years to get Nacho's current age

    # Calculate the sum of their current ages
    total_age_now = divya_age + nacho_age_now
    result = total_age_now
    return result

print(solution())