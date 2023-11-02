def solution():
    """Kris has been suspended for bullying many times. For every instance of bullying, she was suspended for 3 days. If she has been suspended for three times as many days as a typical person has fingers and toes, how many instances of bullying is she responsible for?"""
    typical_person_days = 20  # 10 fingers, 10 toes, 2 days per digit = 20 days total
    kris_days = typical_person_days * 3
    instances_of_bullying = kris_days / 3
    result = instances_of_bullying
    return result

print(solution())