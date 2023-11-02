def solution():
    """Kenneth spent 10% of this earnings this week on a new joystick. If he is left with $405, how much were his earnings?"""
    # Let's assume Kenneth's earnings are x
    # Kenneth spent 10% of his earnings, so he has 0.9x left after buying the joystick
    # We know that this amount is $405, so we can set up an equation: 0.9x = 405
    # Solving for x gives us Kenneth's earnings for the week

    # Solve the equation for x
    x = 405 / 0.9

    # Display Kenneth's earnings
    result = x
    return result

print(solution())