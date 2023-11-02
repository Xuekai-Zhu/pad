def solution():
    """Felix can lift off the ground 1.5 times more than he weighs.
    Felix's brother weighs twice as much as Felix and can lift three times his weight off the ground.
    If his brother can lift 600 pounds, how much can Felix lift off the ground?"""
    brother_weight = 2 * felix_weight
    brother_lift = 3 * brother_weight
    felix_lift = (1.5 * felix_weight) * brother_lift / brother_weight
    result = felix_lift
    return result

print(solution())