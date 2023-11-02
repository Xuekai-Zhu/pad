def solution():
    # Let x be the number of days Johnny has been practicing
    # Let p be the amount of practice Johnny does each day
    # Let a be the amount of practice Johnny had 20 days ago

    p = # fill in the amount of practice Johnny does each day
    a = p * 20 / 2  # Johnny had half as much practice as he currently has 20 days ago
    x = (a + p * 20) / p  # Solve for x using the equation a + p * (x - 20) = 2 * p * x

    # Solve for the number of days required for Johnny to have 3 times as much practice as he does currently
    days_required = (2 * p * x) / (3 * p) - x
    result = days_required
    return result

print(solution())