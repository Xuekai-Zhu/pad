def solution():
    
    red_balls_initial = 16
    blue_balls_initial = 2 * red_balls_initial
    total_initial = red_balls_initial + blue_balls_initial
    red_balls_final = red_balls_initial - 6
    total_final = 74
    yellow_balls = total_final - (red_balls_final + blue_balls_initial)
    result = yellow_balls
    return result

print(solution())