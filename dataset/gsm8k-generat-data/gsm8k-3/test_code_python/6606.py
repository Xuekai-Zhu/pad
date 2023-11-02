def solution():
    """Ali turned 8 years old this year, and is now 3 years older than Yusaf. If Umar is twice Yusaf’s age, how old is Umar?"""
    # Define Ali's age and the age difference between Ali and Yusaf
    ali_age = 8
    ali_yusaf_age_diff = 3

    # Calculate Yusaf's age
    yusaf_age = ali_age - ali_yusaf_age_diff

    # Calculate Umar's age
    umar_age = 2 * yusaf_age

    # Display Umar's age
    result = umar_age
    return result

print(solution())