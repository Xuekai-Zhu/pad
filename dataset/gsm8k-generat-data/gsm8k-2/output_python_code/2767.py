def solution():
    """Robert had 25 balls. Tim gave him half of his 40 balls. How many balls does Robert have now?"""
    robert_balls = 25
    tim_balls = 40
    robert_balls += tim_balls / 2
    result = robert_balls
    return result

print(solution())