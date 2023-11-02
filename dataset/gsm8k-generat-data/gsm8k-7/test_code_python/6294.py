def solution():
    jill_age = 20
    roger_age = 5 + 2*jill_age

    # Calculate the sum of their ages in 15 years
    sum_ages_after_15_years = (jill_age + 15) + (roger_age + 15)

    # Calculate finley's age in 15 years
    finley_age_after_15_years = sum_ages_after_15_years - 30
    
    # Calculate Finley's current age
    finley_age = finley_age_after_15_years - 15

    result = finley_age
    return result

print(solution())