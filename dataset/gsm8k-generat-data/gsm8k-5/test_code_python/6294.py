def solution():
    jill_age = 20  # Jill is 20 years old
    roger_age = 5 + 2 * jill_age  # Roger's age is 5 more than twice Jill's age
    finley_age_diff = 30 + roger_age - jill_age - 15  # Age difference in 15 years will be 30 years less than Finley's age
    finley_age = finley_age_diff + jill_age + 15  # Calculate Finley's age
    result = finley_age
    return result

print(solution())