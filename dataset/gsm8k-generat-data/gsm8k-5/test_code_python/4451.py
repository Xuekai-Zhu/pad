def solution():
    total_mms = 25  # Cheryl had 25 m&m's at the beginning
    mms_eaten_lunch = 7  # Cheryl ate 7 m&m's after lunch
    mms_eaten_dinner = 5  # Cheryl ate 5 m&m's after dinner
    mms_left = total_mms - mms_eaten_lunch - mms_eaten_dinner  # Cheryl has some m&m's left

    # Calculate the number of m&m's Cheryl gave to her sister
    mms_given_to_sister = total_mms - mms_left
    result = mms_given_to_sister
    return result

print(solution())