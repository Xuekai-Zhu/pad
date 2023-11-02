def solution():
    """Felix can lift off the ground 1.5 times more than he weighs. Felix's brother weighs twice as much as Felix and can lift three times his weight off the ground. If his brother can lift 600 pounds, how much can Felix lift off the ground?"""
    brother_weight = 2 * felix_weight
    brother_lift = 3 * brother_weight
    felix_lift = (felix_weight * 1.5) * 1.0  # multiplying by 1.0 to ensure float result
    result = felix_lift
    return result

print(solution())