def solution():
    """In 5 years, Andy will be twice as old as Rahim is now. Rahim is 6 now. How much older is Andy than Rahim, right now, in years?"""
    # Define Rahim's age
    RAHIM_AGE = 6

    # Calculate Andy's age in 5 years
    andy_5years = RAHIM_AGE * 2

    # Calculate Andy's current age
    andy_current = andy_5years - 5

    # Calculate the age difference between Andy and Rahim
    age_difference = andy_current - RAHIM_AGE

    # Display the age difference
    result = age_difference
    return result

print(solution())