def solution():
    
    starting_balls = 3
    weeks_per_month = 4
    balls_added_per_week = 1
    balls_dropped_per_week = 3
    balls_caught_by_crowd = 2
    balls_lost_per_week = 1
    
    total_balls = starting_balls + balls_added_per_week + balls_dropped_per_week - balls_caught_by_crowd - balls_lost_per_week
    total_balls += 4
    
    result = total_balls
    return result

print(solution())