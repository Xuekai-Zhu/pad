def solution():
    phoebe_current_age = 10  # Phoebe is currently 10 years old
    raven_age_difference = 4  # In 5 years, Raven will be 4 times as old as Phoebe
    raven_future_age = phoebe_current_age * raven_age_difference  # Calculate Raven's age in 5 years
    raven_current_age = raven_future_age - 5  # Subtract 5 years to get Raven's current age
    result = raven_current_age
    return result

print(solution())