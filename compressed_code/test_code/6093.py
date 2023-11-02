def solution():
    
    total_balls = 40
    blue_balls = 11
    red_balls = 2 * blue_balls
    green_balls = total_balls - blue_balls - red_balls
    result = green_balls
    return result

print(solution())