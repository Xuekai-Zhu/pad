def solution():
    """Ryan has 40 balls. There are twice as many red balls as blue while the rest are green. If there are 11 blue balls, how many green balls are there?"""
    total_balls = 40
    blue_balls = 11
    red_balls = 2 * blue_balls
    green_balls = total_balls - blue_balls - red_balls
    result = green_balls
    return result

print(solution())