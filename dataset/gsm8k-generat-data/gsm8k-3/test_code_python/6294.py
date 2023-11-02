def solution():
    """Roger's age is 5 more than twice Jill's age. In 15 years, their age difference will be 30 years less than Finley's age. If Jill is 20 years old now, how old is Finley?"""
    # Define Jill's age
    jill_age = 20

    # Calculate Roger's age
    roger_age = 2 * jill_age + 5

    # Determine the age difference between Roger and Jill in 15 years
    age_diff = abs((roger_age + 15) - (jill_age + 15))

    # Determine Finley's age
    finley_age = age_diff + 30

    # Display Finley's age
    result = finley_age
    return result

print(solution())