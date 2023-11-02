def solution():
    """In 5 years, Raven will be 4 times as old as Phoebe. If Phoebe is currently 10 years old, how old is Raven?"""
    # Define Phoebe's current age
    phoebe_age = 10

    # Calculate Raven's age in 5 years
    ravens_age_in_5_years = 4 * (phoebe_age + 5)

    # Calculate Raven's current age
    ravens_age = ravens_age_in_5_years - 5

    result = ravens_age
    return result

print(solution())