def solution():
    """Robert had 25 balls. Tim gave him half of his 40 balls. How many balls does Robert have now?"""
    robert_balls = 25
    tim_balls = 40
    tim_gave = tim_balls / 2
    total_balls = robert_balls + tim_gave
    result = total_balls
    return result

print(solution())