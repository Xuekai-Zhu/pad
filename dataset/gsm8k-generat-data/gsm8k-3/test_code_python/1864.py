def solution():
    """In 5 years, Raven will be 4 times as old as Phoebe. If Phoebe is currently 10 years old, how old is Raven?"""
    # Define Phoebe's current age
    phoebe_age = 10

    # Calculate Raven's age in 5 years
    raven_in_5_years = 4 * (phoebe_age + 5)

    # Calculate Raven's current age
    raven_age = raven_in_5_years - 5

    # Display Raven's current age
    result = raven_age
    return result

print(solution())