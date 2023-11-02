def solution():
    """Kris has been suspended for bullying many times. For every instance of bullying, she was suspended for 3 days. If she has been suspended for three times as many days as a typical person has fingers and toes, how many instances of bullying is she responsible for?"""
    typical_days_suspended = 20 # assuming a typical person has 10 fingers and 10 toes, total of 20
    total_days_suspended = typical_days_suspended * 3 # Kris has been suspended for 3 times as many days
    instances_of_bullying = total_days_suspended // 3 # each instance of bullying results in 3 days of suspension
    result = instances_of_bullying
    return result

print(solution())