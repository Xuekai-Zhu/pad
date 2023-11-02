def solution():
    total_balls = 50
    red_balls = 20
    blue_balls = 10
    pink_balls = (total_balls - red_balls - blue_balls) / 3
    orange_balls = (total_balls - red_balls - blue_balls) - pink_balls
    result = orange_balls
    
    return result

print(solution())