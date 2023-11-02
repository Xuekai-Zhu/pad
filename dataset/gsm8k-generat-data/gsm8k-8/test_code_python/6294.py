def solution():
    # Define Jill's age
    jill_age = 20

    # Calculate Roger's age
    roger_age = 2 * jill_age + 5

    # Calculate the age difference between Roger and Jill in 15 years
    age_diff_in_15_years = abs(roger_age - jill_age - 15)

    # Calculate Finley's current age
    finley_age = age_diff_in_15_years + 30

    result = finley_age
    return result

print(solution())