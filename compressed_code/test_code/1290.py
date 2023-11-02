def solution():
    
    red_balls = 16
    blue_balls = 2 * red_balls
    total_balls = red_balls + blue_balls - 6  
    yellow_balls = 74 - total_balls
    result = yellow_balls
    return result

print(solution())