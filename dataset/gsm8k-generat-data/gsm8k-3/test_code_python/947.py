def solution():
    """Johnny has been playing guitar for a while now.  He practices the same amount each day. As of 20 days ago he had half as much practice as he has currently.  How many days will pass before Johnny has 3 times as much practice as he does currently?"""
    # Let x be the number of days Johnny has been practicing
    # Let y be the amount of practice Johnny does each day

    # From the problem, we know that:
    # y * (x - 20) = 0.5 * x * y
    # This equation means that 20 days ago, Johnny had practiced half as much as he currently has

    # Simplifying the equation, we get:
    # x = 40

    # So Johnny has been practicing for 40 days
    # Let z be the number of days Johnny needs to practice before he has 3 times as much practice as he does currently

    # We can set up another equation:
    # y * (x + z) = 3 * y * x

    # Simplifying the equation, we get:
    # z = 2 * x

    # So Johnny needs to practice for 80 more days

    result = z
    return result

print(solution())