def solution():
    # Find Raven's age in 5 years
    raven_in_5_years = 4 * (10 + 5)  # Phoebe is currently 10, so in 5 years she'll be 15. Raven's age in 5 years will be 4 times Phoebe's age in 5 years.
    
    # Find Raven's current age
    raven_age = raven_in_5_years - 5  # Raven's age in 5 years minus the time that has passed
    
    result = raven_age
    return result

print(solution())