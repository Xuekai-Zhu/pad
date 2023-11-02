def solution():
    
    initial_balls = 3
    balls_added_per_week = 1
    total_balls = initial_balls + balls_added_per_week
    lost_balls = 2
    total_balls -= lost_balls + balls_added_per_week
    result = total_balls
    return result

print(solution())