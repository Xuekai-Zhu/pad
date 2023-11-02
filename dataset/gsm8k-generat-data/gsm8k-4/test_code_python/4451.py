def solution():
    """Cheryl ate 7 m&m's after lunch. She ate 5 m&m's after dinner, and she gave some to her sister. If Cheryl had 25 m&m's at the beginning, how many did she give to her sister?"""
    # Define the number of m&m's Cheryl had at the beginning
    initial_mms = 25

    # Calculate the number of m&m's Cheryl had after lunch and dinner
    mms_after_lunch = initial_mms - 7
    mms_after_dinner = mms_after_lunch - 5

    # Calculate the number of m&m's Cheryl gave to her sister
    mms_to_sister = initial_mms - mms_after_dinner

    # return the result
    result = mms_to_sister
    return result

print(solution())