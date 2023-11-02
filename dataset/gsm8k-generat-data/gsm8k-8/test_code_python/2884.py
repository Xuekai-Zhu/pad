def solution():
    # Let Felix's weight be x
    # Felix can lift off the ground 1.5 times more than he weighs, so he can lift 2.5x
    # Let Felix's brother's weight be 2x
    # Felix's brother can lift three times his weight, so he can lift 6x = 600 pounds
    # Solving for x, we get x = 100, which is Felix's weight
    felix_lift = 2.5 * 100 # Felix can lift 2.5 times his weight
    result = felix_lift
    return result

print(solution())