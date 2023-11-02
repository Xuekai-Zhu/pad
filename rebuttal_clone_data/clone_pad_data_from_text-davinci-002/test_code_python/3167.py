def solution():
    minutes_per_ball = 20
    balls_inflated_by_alexia = 20
    balls_inflated_by_ermias = balls_inflated_by_alexia + 5
    total_balls = balls_inflated_by_alexia + balls_inflated_by_ermias
    total_minutes = total_balls * minutes_per_ball
    result = total_minutes
    
    return result

print(solution())