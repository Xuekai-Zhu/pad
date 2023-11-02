def solution():
    """Roger's age is 5 more than twice Jill's age. In 15 years, their age difference will be 30 years less than Finley's age. If Jill is 20 years old now, how old is Finley?"""
    jill_age = 20
    roger_age = 2 * jill_age + 5
    age_difference_now = roger_age - jill_age
    finley_age_difference = age_difference_now - 30
    finley_age_in_15_years = finley_age_difference + (jill_age + 15) + (roger_age + 15)
    finley_age = finley_age_in_15_years - 15
    result = finley_age
    return result

print(solution())