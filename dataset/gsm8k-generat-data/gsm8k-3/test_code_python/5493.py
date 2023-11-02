def solution():
    """Christina's age will be half of 80 years in five years to come. If Oscar will be 3/5 times as old as Christina is now in 15 years, calculate Oscar's age now."""
    # Calculate Christina's age in 5 years
    christina_age_in_5_years = 0.5 * 80

    # Calculate Christina's current age
    christina_age_now = christina_age_in_5_years - 5

    # Calculate Oscar's age in 15 years
    oscar_age_in_15_years = (3/5) * christina_age_now + 15

    # Calculate Oscar's current age
    oscar_age_now = oscar_age_in_15_years - 15

    # Display Oscar's current age
    result = oscar_age_now
    return result

print(solution())