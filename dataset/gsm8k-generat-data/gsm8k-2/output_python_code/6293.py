def solution():
    """Roger's age is 5 more than twice Jill's age. In 15 years, their age difference will be 30 years less than Finley's age. If Jill is 20 years old now, how old is Finley?"""
    jill_age = 20
    roger_age = 2 * jill_age + 5
    finley_age_difference = (roger_age + 15 - (jill_age + 15)) - 30
    finley_age = finley_age_difference + (jill_age + 15)
    result = finley_age
    return result

print(solution())