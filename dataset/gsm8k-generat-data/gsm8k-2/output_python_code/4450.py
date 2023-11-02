def solution():
    """Cheryl ate 7 m&m's after lunch. She ate 5 m&m's after dinner, and she gave some to her sister. If Cheryl had 25 m&m's at the beginning, how many did she give to her sister?"""
    initial_mms = 25
    lunch_mms = 7
    dinner_mms = 5
    cheryl_mms = lunch_mms + dinner_mms
    sister_mms = initial_mms - cheryl_mms
    result = sister_mms
    return result

print(solution())