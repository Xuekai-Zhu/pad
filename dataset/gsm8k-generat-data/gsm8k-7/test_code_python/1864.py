def solution():
    # Set Phoebe's age
    phoebe_age = 10

    # Set the age difference between Raven and Phoebe in 5 years
    age_difference = 4

    # Calculate Raven's age in 5 years
    raven_age_in_5_years = age_difference * (phoebe_age + 5)

    # Calculate Raven's current age
    raven_age = raven_age_in_5_years - 5

    result = raven_age
    return result

print(solution())