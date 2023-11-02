def solution():
    # Let x be the number of days Johnny has been practicing
    # We know that x - 20 represents the number of days since Johnny had half as much practice as he has currently
    # We also know that 3 times Johnny's current practice is equal to 6 times the practice from x - 20 days ago
    # So, we can write the equation:
    # 3x = 6(x - 20)/2

    x = 120  # solve for x, x = 120 days

    # Therefore, Johnny will need to practice for another 200 days (3 times his current practice) - 120 days (current practice)
    # in order to have 3 times as much practice as he does currently
    days_to_practice = 200 - 120

    result = days_to_practice
    return result

print(solution())