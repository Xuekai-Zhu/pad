def solution():
    """Roger's age is 5 more than twice Jill's age. In 15 years, their age difference will be 30 years less than Finley's age. If Jill is 20 years old now, how old is Finley?"""
    # Define Jill's age
    jill_age = 20

    # Calculate Roger's age
    roger_age = 2*jill_age + 5

    # Calculate the current age difference between Roger and Jill
    age_difference = roger_age - jill_age

    # Define the number of years in the future
    years_in_future = 15

    # Calculate the age difference between Roger and Jill in the future
    future_age_difference = age_difference + years_in_future

    # Calculate Finley's current age
    finley_age = future_age_difference + 30

    # return the result
    result = finley_age
    return result

print(solution())