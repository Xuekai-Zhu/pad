def solution():
    typical_suspension_days = 5 * 3  # 5 fingers + 5 toes = 10 digits => 10 * 3 = 30 days
    kris_suspension_days = typical_suspension_days * 3  # Kris has been suspended for three times as many days as a typical person
    instances_of_bullying = kris_suspension_days / 3  # Kris was suspended for 3 days for each instance of bullying
    result = instances_of_bullying
    return result

print(solution())