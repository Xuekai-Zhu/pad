def solution():
    # Find Roger's age
    roger_age = 2 * 20 + 5  # Roger's age is 5 more than twice Jill's age

    # Find the difference in ages between Jill and Roger in 15 years
    jill_age_in_15_years = 20 + 15
    roger_age_in_15_years = roger_age + 15
    age_difference = abs(jill_age_in_15_years - roger_age_in_15_years)

    # Find Finley's current age
    finley_age = age_difference + 30
    result = finley_age
    return result

print(solution())