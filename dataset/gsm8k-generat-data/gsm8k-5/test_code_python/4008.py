def solution():
    typical_suspension_days = 3 * 10  # A typical person has 10 fingers and 10 toes, so 3 days per finger/toe
    total_suspension_days = typical_suspension_days * 3  # Kris has been suspended for three times as many days
    instances_of_bullying = total_suspension_days / 3  # Kris was suspended for 3 days per instance of bullying
    result = instances_of_bullying
    return result

print(solution())