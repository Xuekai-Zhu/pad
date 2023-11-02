def solution():
    """Cheryl ate 7 m&m's after lunch. She ate 5 m&m's after dinner, and she gave some to her sister. If Cheryl had 25 m&m's at the beginning, how many did she give to her sister?"""
    mms_after_lunch = 7
    mms_after_dinner = 5
    total_mms_eaten = mms_after_lunch + mms_after_dinner
    mms_left = 25 - total_mms_eaten
    mms_given_away = mms_left
    result = mms_given_away
    return result

print(solution())