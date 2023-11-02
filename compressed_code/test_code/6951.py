def solution():
    
    total_balls = 50
    red_balls = 20
    blue_balls = 10
    pink_orange_balls = total_balls - red_balls - blue_balls
    pink_balls = 3 * pink_orange_balls / 4
    orange_balls = pink_orange_balls - pink_balls
    result = orange_balls
    return result

print(solution())