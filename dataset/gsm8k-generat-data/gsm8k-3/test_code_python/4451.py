def solution():
    """Cheryl ate 7 m&m's after lunch. She ate 5 m&m's after dinner, and she gave some to her sister. If Cheryl had 25 m&m's at the beginning, how many did she give to her sister?"""
    # Cheryl had 25 m&m's at the beginning
    total_mms = 25

    # Cheryl ate 7 m&m's after lunch
    total_mms -= 7

    # Cheryl ate 5 m&m's after dinner
    total_mms -= 5

    # The remaining m&m's are the ones Cheryl gave to her sister
    mms_given_away = total_mms

    # Display the number of m&m's Cheryl gave to her sister
    result = mms_given_away
    return result

print(solution())