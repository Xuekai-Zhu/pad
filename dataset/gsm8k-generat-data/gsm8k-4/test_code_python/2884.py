def solution():
    """Felix can lift off the ground 1.5 times more than he weighs. Felix's brother weighs twice as much as Felix and can lift three times his weight off the ground. If his brother can lift 600 pounds, how much can Felix lift off the ground?"""
    # Define Felix's weight
    felix_weight = None

    # Define Felix's lifting capacity
    felix_lift = None

    # Define Felix's brother's weight
    brother_weight = felix_weight * 2

    # Define Felix's brother's lifting capacity
    brother_lift = brother_weight * 3

    # Use the given information to calculate Felix's weight and lifting capacity
    felix_weight = brother_weight / 2
    felix_lift = felix_weight * 1.5

    result = felix_lift
    return result

print(solution())